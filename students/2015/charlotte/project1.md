#Project 1

## Melting Styrofoam

I put a HD webcam on a mini robot arm to get more control over the scenes I created. These scenes were melting styrofoam sculptures.

[![](images/styro1.gif)](https://vimeo.com/140208062)

Code to control and sync robot arm and camera:

```
/************************************************************************
* File Name          : uArm_Client
* Author             : Evan
* Updated            : Alex
* Version            : V0.65
* Date               : 23 Apr, 2015
* Description        : Processing to control uArm using LeapMotion
                       using the "Standard.ino" on uArm.
                       Need G4P library and LeapMotionForProcessing library.
* Update Note        : V0.6  Slider2d support Mouse move without drag. armHeight slider support Mouse wheel - 10-Apr-2015
                       V0.65 Myo Control, UDP socket Control  - 23-Apr-2015
* Copyright(C) 2014 UFactory Team. All right reserved.
*************************************************************************/

//This code also takes from Epic Jefferson- https://github.com/epicjefferson/Computing4CreativePractice/tree/master/uArm_Client
//and Golan Levin- https: //github.com/golanlevin/ExperimentalCapture/tree/master/code/time_lapse/time_lapse_processing_v221_2ndcam
//Many thanks!

import processing.serial.*;
import java.awt.*;
import javax.swing.*;

int pause = 100; // milliseconds between frames

int videoWidth; 
int videoHeight;

int x = 100;
int y = 0;
int z;


import  processing.video.*;
Capture myCapture;

boolean UPDATE_EN = false;

String ip = "0.0.0.0";
int port = 0;

int yOff = 80;

int oldX;
int oldY;

public void setup()
{
  scanPort();
  videoWidth = 1920;
  videoHeight = 1080;

  myCapture = new Capture(this, videoWidth, videoHeight, "Logitech Camera", 15);
  myCapture.start();   
  
  size(myCapture.width, myCapture.height);

}

public void draw()
{ 
  if(UPDATE_EN)
  {
    sendPos(y, x, z, 0, byte(0));
    UPDATE_EN = false;
  }

  if (myCapture.available()) {
    
    myCapture.read();
    image(myCapture, 0, 0); 
    long now = millis();
    if ((now - lastCaptureTime) >= pause) {
      String filename = "timelapse_" + nf(saveCount, 6) + ".jpg";
      saveFrame(filename);
      lastCaptureTime = now;
      saveCount++;
      if (yOff > -40){
        if (saveCount % 5 ==0){
          yOff = yOff + 2;
           x = x -3;  
      }
          
      }
      else{yOff = -40;} 
    }
  }
  y = yOff;
  UPDATE_EN = true;
}
```