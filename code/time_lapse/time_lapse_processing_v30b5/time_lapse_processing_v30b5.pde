// TINY TIME-LAPSE PROGRAM
// Saves an image from the camera once per second,
// or at some other user-defined interval.
// For Processing Version 3.0b5.
// You'll need to "install" the Processing Video library. 

//----------------------------------------------------------
// Parameters you can modify
int videoWidth  = 320; // could be 160, 320, 640, etc.
int videoHeight = 240; // could be 120, 240, 480, etc.
int     period = 1000; // milliseconds between frames
 
//----------------------------------------------------------
import  processing.video.*;
Capture myCapture;
long    lastCaptureTime = 0;
int     saveCount = 0;
 
//----------------------------------------------------------
void setup(){
  
  myCapture = new Capture(this, 320,240);
  myCapture.start(); 
  size(320,240);
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