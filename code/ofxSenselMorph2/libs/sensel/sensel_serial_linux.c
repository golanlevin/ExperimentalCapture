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

#include "sensel_serial.h"
#include "sensel.h"
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <termios.h>
#include <dirent.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/select.h>

extern bool _readReg(uint8 reg, uint8 size, uint8 *buf);

#define SENSEL_SERIAL_DIR "/dev/"

//TODO: Add a separate for flushing data
#define SENSEL_SERIAL_TIMEOUT_SEC 0
#define SENSEL_SERIAL_TIMEOUT_US  (500 * 1000) //500 ms

bool senselSerialWrite(sensel_serial_data *data, uint8 *buf, int buf_len)
{
  int wr = write(data->serial_fd, buf, buf_len);

  //THIS CAUSES READ FAILURE IN MAC OSX!!! tcflush(data->serial_fd, TCOFLUSH);

  if(wr == -1)
  {
    perror("FAILED TO WRITE TO DEVICE");
    return false;
  }
  return true;
}

int senselSerialReadAvailable(sensel_serial_data *data, uint8 *buf, int buf_len)
{
  fd_set read_fds;
  FD_ZERO(&read_fds);
  FD_SET(data->serial_fd, &read_fds);

  //select() changes timeout value, so we need this on every call to readAvailable
  struct timeval timeout;
  timeout.tv_sec = SENSEL_SERIAL_TIMEOUT_SEC;
  timeout.tv_usec = SENSEL_SERIAL_TIMEOUT_US;

  //select() uses fd + 1
  int ret = select(data->serial_fd + 1, &read_fds, NULL, NULL, &timeout);

  if(ret == -1) //Select error
  {
    perror("Error on select()");
    return -1;
  }
  else if (ret > 0) //We have bytes to read!
  {
    ret = read(data->serial_fd, buf, buf_len);

    if(ret < 0)
      perror("read returned -1");

    return ret;
  }
  else //No data available after timeout
  {
    printf("select() timedout with no data, ret=%d\n", ret);
    return 0;
  }
}

bool senselSerialReadBytes(sensel_serial_data *data, uint8 *buf, int buf_len)
{
  int max_attempts = 1;
  int failed_attempts = 0;
  int bytes_left = buf_len;

  do
  {
    int bytes_read = senselSerialReadAvailable(data, buf, bytes_left);

    if(bytes_read <= 0)
    {
      failed_attempts++;
    }
    else
    {
      buf += bytes_read;
      bytes_left -= bytes_read;
    }

    if(failed_attempts >= max_attempts)
    {
      return false;
    }
  }
  while(bytes_left > 0);

  return true;
}

// TODO: Test on Linux
int senselSerialGetAvailable(sensel_serial_data *data)
{
  int bytes_avail;
  ioctl(data->serial_fd, FIONREAD, &bytes_avail);

  return bytes_avail;
}

void senselSerialFlushInput(sensel_serial_data *data)
{
  int bytes_read = 0;
  int byte_total = 0;
  unsigned char buf[128];

  //Read while there are bytes available
  do
  {
    bytes_read = senselSerialReadAvailable(data, buf, 128);
    byte_total += bytes_read;
  }
  while(bytes_read > 0);

  printf("Cleared %d bytes from buffer!\n", byte_total);
}

bool senselSerialOpen2(sensel_serial_data * data, char* file_name)
{
  char magic[7];
  magic[6] = '\0';

  printf("Opening %s...", file_name);

  data->serial_fd = open(file_name, O_RDWR | O_NONBLOCK | O_NOCTTY);

  if(data->serial_fd == -1)
  {
    printf("unable to open!\n");
    return false;
  }

  struct termios options;
  tcgetattr(data->serial_fd, &options);
  cfmakeraw(&options);
  cfsetispeed(&options, B115200);
  cfsetospeed(&options, B115200);
  tcsetattr(data->serial_fd, TCSANOW, &options);

  senselSerialFlushInput(data);

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

  close(data->serial_fd);
  data->serial_fd = -1;
  return false;
}

bool senselSerialOpen(sensel_serial_data * data, char* com_port)
{
  DIR *d;
  struct dirent *dir;
  char file_name[100];
  bool found_sensor = false;

  if(com_port != NULL)
  {
    return senselSerialOpen2(data, com_port);
  }

  d = opendir(SENSEL_SERIAL_DIR);
  if(!d)
  {
    printf("Could not open %s directory.", SENSEL_SERIAL_DIR);
    return false;
  }

  while((dir = readdir(d)) != 0)
  {
    strcpy(file_name, SENSEL_SERIAL_DIR);

    if(strstr(dir->d_name, "ttyS") || 
       strstr(dir->d_name, "ttyUSB") || 
       strstr(dir->d_name, "tty.usbmodem") || 
       strstr(dir->d_name, "cu.usbmodem") || 
       strstr(dir->d_name, "ttyACM"))
    {
      strcat(file_name, dir->d_name);

      found_sensor = senselSerialOpen2(data, file_name);
      if(found_sensor)
      {
        break;
      }
    }
  }
  closedir(d);

  return found_sensor;
}

void senselSerialClose(sensel_serial_data *data)
{
  if(data->serial_fd != -1)
  {
    close(data->serial_fd);
    data->serial_fd = -1;
  }
}
