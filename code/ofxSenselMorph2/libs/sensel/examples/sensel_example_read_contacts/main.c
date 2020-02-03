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
 * This opens a Sensel sensor, reads contact data, and prints the data to the console.
 */

//Inclue a sleep function
#ifdef WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include <stdio.h>
#include <signal.h> //so we can catch a ctrl+c key event
#include "sensel.h"

volatile sig_atomic_t ctrl_c_requested = false;

contact_t *contacts;
int n_contacts = 0;

void handle_ctrl_c(int sig)
{
  ctrl_c_requested = true;
}

int main()
{
  signal (SIGINT, handle_ctrl_c);

  bool sensel_sensor_opened = false;

  sensel_sensor_opened = senselOpenConnection(0);
  
  if(!sensel_sensor_opened)
  {
    printf("Unable to open Sensel sensor!\n");
    return -1;
  }
  
  //Enable contact sending
  senselSetFrameContentControl(SENSEL_FRAME_CONTENT_CONTACTS_MASK);
  
  //Enable scanning
  senselStartScanning();

  printf("Touch sensor! (press ctrl-c to quit)...\n");

  while(!ctrl_c_requested)
  {
    senselReadFrame(&contacts, &n_contacts, NULL, NULL);
  
    for(int i = 0; i < n_contacts; i++)
    {
      float force = contacts[i].total_force;
      float x_mm = contacts[i].x_pos_mm;
      float y_mm = contacts[i].y_pos_mm;
      //Read out shape information (ellipses)
      float major = contacts[i].major_axis_mm;
      float minor = contacts[i].minor_axis_mm;
      float orientation = contacts[i].orientation_degrees;

      int id = contacts[i].id;
      int event_type = contacts[i].type;
      
      char* event;
      switch (event_type)
      {
        case SENSEL_EVENT_CONTACT_INVALID:
          event = "invalid";
          break;
        case SENSEL_EVENT_CONTACT_START:
          senselSetLEDBrightness(id, 100); //turn on LED
          event = "start";
          break;
        case SENSEL_EVENT_CONTACT_MOVE:
          event = "move";
          break;
        case SENSEL_EVENT_CONTACT_END:
          senselSetLEDBrightness(id, 0); //turn LED off
          event = "end";
          break;
        default:
          event = "error";
      }
      
      printf("Contact ID %d, event=%s, mm coord: (%f, %f), force=%f, " \
             "major=%f, minor=%f, orientation=%f\n", 
             id, event, x_mm, y_mm, force, major, minor, orientation);
    }
    
    if(n_contacts > 0)
      printf("****\n");
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


