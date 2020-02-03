/**************************************************************************
 * Copyright 2015 Sensel, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 **************************************************************************/

#include "stdafx.h"
#include "sensel_serial.h"

#define SENSEL_COM_PORT_PREFIX "\\\\.\\"
extern "C" bool _readReg(uint8 reg, uint8 size, uint8 *buf);

bool senselSerialOpen2(sensel_serial_data *data, char* com_port)
{
  DCB dcb;
  COMMTIMEOUTS timeouts;
  BOOL fSuccess;
  char full_port_name[100];
  char magic[7];
  magic[6] = '\0';

  strcpy_s(full_port_name, SENSEL_COM_PORT_PREFIX);
  strcat_s(full_port_name, com_port);

  data->serial_handle = CreateFile(TEXT(full_port_name),
                    GENERIC_READ | GENERIC_WRITE,
                    0,    // must be opened with exclusive-access
                    NULL, // no security attributes
                    OPEN_EXISTING, // must use OPEN_EXISTING
                    FILE_ATTRIBUTE_NORMAL,    // not overlapped I/O
                    NULL  // hTemplate must be NULL for comm devices
                    );

  if (data->serial_handle == INVALID_HANDLE_VALUE) 
  {
    // Handle the error.
    printf ("CreateFile failed with error %d.\n", GetLastError());
    return false;
  }

  // Build on the current configuration, and skip setting the size
  // of the input and output buffers with SetupComm.
  fSuccess = GetCommState(data->serial_handle, &dcb);
  if (!fSuccess) 
  {
    // Handle the error.
    printf ("GetCommState failed with error %d.\n", GetLastError());
    senselSerialClose(data);
    return false;
  }

  // Fill in DCB: 115,200 bps, 8 data bits, no parity, and 1 stop bit.
  dcb.BaudRate = CBR_115200;    // CBR_9600;  // set the baud rate
  dcb.ByteSize = 8;             // data size, xmit, and rcv
  dcb.Parity = NOPARITY;        // no parity bit
  dcb.StopBits = ONESTOPBIT;    // one stop bit

  // The following settings are probably not necessary
  dcb.DCBlength = sizeof(dcb);
  dcb.fBinary = TRUE;
  dcb.fDtrControl = DTR_CONTROL_DISABLE;
  dcb.fRtsControl = RTS_CONTROL_DISABLE;
  dcb.fOutxCtsFlow = FALSE;
  dcb.fOutxDsrFlow = FALSE;
  dcb.fDsrSensitivity= FALSE;
  dcb.fAbortOnError = TRUE;

  fSuccess = SetCommState(data->serial_handle, &dcb);
  if (!fSuccess) 
  {
    // Handle the error.
    printf("SetCommState failed with error %d.\n", GetLastError());
    senselSerialClose(data);
    return false;
  }

  GetCommTimeouts(data->serial_handle, &timeouts);

  timeouts.ReadIntervalTimeout = 50; // If 50ms elapses after the last byte read, the read function times out
  timeouts.ReadTotalTimeoutConstant = 50; // For each byte that we try to read, allow a maximum of 50ms...
  timeouts.ReadTotalTimeoutMultiplier = 10; // Plus a constant delay of 10ms
  timeouts.WriteTotalTimeoutConstant = 50; // For each byte that we try to write, allow a maximum of 50ms...
  timeouts.WriteTotalTimeoutMultiplier= 10; // Plus a constant delay of 10ms

  if(!SetCommTimeouts(data->serial_handle, &timeouts)) 
  {
    printf("SetCommTimeouts failed.");
  }

  /*
  if(!SetupComm(data->serial_handle, 40000, 40000))
  {
    printf("Error setting buffer size.");
  }
  */

  printf("Serial port %s successfully connected.\n", com_port);
  
  // Flush out any characters that might be in the serial receive buffer
  senselSerialFlushInput(data);

  // Check for the magic number
  if(_readReg(0x00, SENSEL_MAGIC_LEN, (uint8*)magic))
  {
    printf("Magic: %s\n", magic);
    if(strcmp(magic, SENSEL_MAGIC) == 0)
    {
      printf("Found sensor!\n");
      return true;
    }
    else
    {
      printf("Invalid magic!\n");
    }
  }
  else
  {
    printf("Timeout on read!\n");
  }

  senselSerialClose(data);
  return false;
}

bool senselSerialOpen(sensel_serial_data *data, char* com_port)
{
  char file_name[100];

  if(com_port != NULL)
  {
    return senselSerialOpen2(data, com_port);
  }

  for(int i = 1; i < 256; i++)
  {
    sprintf_s(file_name, "COM%d", i);

    if(senselSerialOpen2(data, file_name))
    {
      return true;
    }
  }

  return false;
}

void senselSerialFlushInput(sensel_serial_data *data)
{
  int bytes_read = 0;
  int byte_total = 0;
  unsigned char buf[128];

  do
  {
    //Try reading a byte
    bytes_read = senselSerialReadAvailable(data, buf, 128);
    if(bytes_read > 0) // We read a byte!
      byte_total += bytes_read;
  }
  while(bytes_read > 0);

  printf("Cleared %d bytes from buffer!\n", byte_total);
}

bool senselSerialWrite(sensel_serial_data *data, uint8* buf, int bufLen)
{
  DWORD dwBytesWritten = 0;

  if(!WriteFile(data->serial_handle, buf, bufLen, &dwBytesWritten, NULL)) 
  { 
    printf("error writing to output buffer");
    return false;
  }

  if(dwBytesWritten != bufLen)
  {
    printf("error only %d out of %d bytes written", dwBytesWritten, bufLen);
    return false;
  }

  //printf("Data written to write buffer is %s", buffWrite);
  return true;
}

// Reads as many bytes as available, up to bufLen, returns number of bytes read or -1 on error
int senselSerialReadAvailable(sensel_serial_data *data, uint8* buf, int bufLen)
{
  //buffRead = 0;
  DWORD dwBytesRead = 0;

  if (!ReadFile(data->serial_handle, buf, bufLen, &dwBytesRead, NULL)) 
  {
    printf("error reading from input buffer");
    return -1;
  }
  
  return dwBytesRead;
}

// Reads a requested number of bytes, returns true on success, false on failure
bool senselSerialReadBytes(sensel_serial_data *data, uint8* buf, int bufLen)
{
  int max_attempts = 3;
  int attempts = 0;

  do
  {
    int bytes_read = senselSerialReadAvailable(data, buf, bufLen);
    if(bytes_read == -1) return false;
    buf += bytes_read;
    bufLen -= bytes_read;

    if(bytes_read == 0)
      attempts++;

    if(attempts >= max_attempts)
    {
      return false;
    }
  }
  while(bufLen > 0);

  return true;
}

int senselSerialGetAvailable(sensel_serial_data *data)
{
  COMSTAT comStatStruct;

  if(!ClearCommError(data->serial_handle, 0, &comStatStruct))
  {
    printf("SENSEL ERROR: Could not get number of available bytes on serial port.\n");
    return 0;
  }

  //printf("Num Chars: %d\n", comStatStruct.cbInQue);

  return comStatStruct.cbInQue;
}

void senselSerialClose(sensel_serial_data *data)
{
  if(data->serial_handle != INVALID_HANDLE_VALUE)
  {
    CloseHandle(data->serial_handle);
    data->serial_handle = INVALID_HANDLE_VALUE;
  }
}
