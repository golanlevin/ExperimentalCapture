// TINY TIME-LAPSE PROGRAM
// Saves an image from the camera once per second,
// or at some other user-defined interval.
// For Processing Version 4.01+
// You'll need to "install" the Processing Video library. 

//----------------------------------------------------------
// Parameters you can modify
int videoWidth  = 640; 
int videoHeight = 480; 
int     period = 1000; // milliseconds between frames
 
//----------------------------------------------------------
import  processing.video.*;
Capture myCapture;
long    lastCaptureTime = 0;
int     saveCount = 0;
 
//----------------------------------------------------------
void setup(){
  size(640,480);
  myCapture = new Capture(this, videoWidth,videoHeight);
  myCapture.start(); 
}
 
//----------------------------------------------------------
void draw() {
  if(myCapture.available()) {
    myCapture.read();
    image(myCapture, 0,0); 
 
    long now = millis();
    if ((now - lastCaptureTime) >= period){
      String filename = "timelapse_" + nf(saveCount, 6) + ".jpg";
      saveFrame(filename);
      lastCaptureTime = now;
      saveCount++;
    }
  }
}
