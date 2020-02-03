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
/**
 * Read Contacts
 * by Aaron Zarraga - Sensel, Inc
 * 
 * This opens a Sensel sensor, reads frame data, and prints the data to the console.
 */

//Inclue a sleep function
#ifdef WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <signal.h> //so we can catch a ctrl+c key event
#include "sensel.h"

volatile sig_atomic_t ctrl_c_requested = false;

contact_t *contacts;
int n_contacts = 0;
float *forces;
uint8 *labels;
int decompressed_cols = 0;
int decompressed_rows = 0;

void handle_ctrl_c(int sig)
{
  ctrl_c_requested = true;
}

int main()
{
	float total_force;
  signal (SIGINT, handle_ctrl_c);

  bool sensel_sensor_opened = false;

  sensel_sensor_opened = senselOpenConnection(0);
  if(!sensel_sensor_opened)
  {
    printf("Unable to open Sensel sensor!\n");
    return -1;
  }

  //Enable frames and labels
  senselSetFrameContentControl(SENSEL_FRAME_CONTENT_PRESSURE_MASK | SENSEL_FRAME_CONTENT_LABELS_MASK);
  
	decompressed_cols = senselDecompressGetCols();
	decompressed_rows = senselDecompressGetRows();
  //Enable scanning
  senselStartScanning();

  printf("Touch sensor! (press ctrl-c to quit)...\n");

	while (!ctrl_c_requested)
	{
		total_force = 0;
		senselReadFrame(&contacts, &n_contacts, &forces, &labels);

		for (int i = 0; i < decompressed_rows; i++)
		{
			for (int j = 0; j < decompressed_cols; j++) {
				total_force = total_force + (forces[i*decompressed_cols + j]);
			}
		}
		printf("Total Force: %f\n", total_force);
  }

  printf("Closing application\n");

  if(sensel_sensor_opened)
  {
#ifdef WIN32
	Sleep(1000);
#else
    sleep(1); //Let ctrl-c-trashed packets clear out
#endif
    senselSetLEDBrightnessAll(0);
    senselStopScanning();
    senselCloseConnection();
  }
  printf("Done!\n");
}


