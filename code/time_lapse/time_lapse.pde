// TINY TIME-LAPSE PROGRAM
// Saves a time lapse video from the camera once per second,
// or at some other user-defined interval.
// For Processing Version 3.5.3+.
// You'll need to "install" the Processing Video library, 
// and the Videi Export library.

//----------------------------------------------------------
// Parameters you can modify
int videoWidth  = 1280; // could be 160, 320, 640, etc.
int videoHeight = 720; // could be 120, 240, 480, etc.
int     period = 1000; // milliseconds between frames
 
//----------------------------------------------------------
import  processing.video.*;
import  com.hamoid.*;

Capture myCapture;
VideoExport videoExport;

long    lastCaptureTime = 0;
int     saveCount = 0;
 
//----------------------------------------------------------
void setup(){
  
  myCapture = new Capture(this, 1280,720);
  myCapture.start(); 
  
  String timelapseFilename = "data/timelapse_" + nf(day(),2) + nf(hour(),2) + nf(minute(),2) + ".mp4"; 
  videoExport = new VideoExport(this, timelapseFilename, myCapture);
  videoExport.startMovie();
  
  size(1280,720);
}
 
//----------------------------------------------------------
void draw() {
  if(myCapture.available()) {
    myCapture.read();
    image(myCapture, 0,0); 
 
    long now = millis();
    if ((now - lastCaptureTime) >= period){
      // String filename = "data/timelapse_" + nf(saveCount, 6) + ".jpg";
      // saveFrame(filename);
      
      videoExport.saveFrame();
      lastCaptureTime = now;
      saveCount++;
    }
  }
}

//----------------------------------------------------------
void keyPressed() {
  if (key == 'q') {
    videoExport.endMovie();
    exit();
  }
}
