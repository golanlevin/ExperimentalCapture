// TINY TIME-LAPSE PROGRAM
// Saves an image from the camera once per second
// (or at some other user-defined interval)
// For Processing Version 4.01+
//
// You'll need to install the "Video Library for Processing 4".
// To install this: Sketch->Import Library...->Manage Libraries...

//----------------------------------------------------------
// Parameters you can modify:
int period = 1000; // milliseconds between frames
int videoWidth  = 1280; 
int videoHeight = 720; 
int whichCameraID = 0; 

//----------------------------------------------------------
import  processing.video.*;
Capture myCapture;
long    lastCaptureTime = 0;
int     saveCount = 0;
String  folderName;
 
//----------------------------------------------------------
void setup(){
  size(1280,720);
  String[] cameras = Capture.list();
  printArray(cameras); // List the available cameras

  myCapture = new Capture(this, videoWidth, videoHeight, cameras[whichCameraID]);
  myCapture.start(); 
  folderName = year() + nf(month(),2) + nf(day(),2) + nf(hour(),2) + nf(minute(),2) + "/"; 
}
 
//----------------------------------------------------------
void draw() {
  if(myCapture.available()) {
    myCapture.read();
    image(myCapture, 0,0); 
 
    long now = millis();
    if ((now - lastCaptureTime) >= period){
      String filename = folderName + "timelapse_" + nf(saveCount, 6) + ".jpg";
      saveFrame(filename);
      lastCaptureTime = now;
      saveCount++;
    }
  }
}
