// TINY TIME-LAPSE PROGRAM
// Saves an image from the camera once per second,
// or at some other user-defined interval, 
// captured from a specific camera.
// For Processing Version 2.2.1.

//----------------------------------------------------------
// Parameters you can modify
int videoWidth; 
int videoHeight;
int period = 1000; // milliseconds between frames

//----------------------------------------------------------
import  processing.video.*;
Capture myCapture;
long    lastCaptureTime = 0;
int     saveCount = 0;

//----------------------------------------------------------
void setup() {

  videoWidth = 1920;
  videoHeight = 1080;

  // Get the list of all available cameras and devices
  String[] cameras = Capture.list();
  for (int i = 0; i < cameras.length; i++) {
    println(i+ " " + cameras[i]);
  }

  // Using the exact name of the camera we want (as printed from the list above:
  myCapture = new Capture(this, videoWidth, videoHeight, "Logitech Camera", 15);
  myCapture.start(); 
  size(myCapture.width, myCapture.height);
}

//----------------------------------------------------------
void draw() {
  if (myCapture.available()) {
    myCapture.read();
    image(myCapture, 0, 0); 

    long now = millis();
    if ((now - lastCaptureTime) >= period) {
      String filename = "timelapse_" + nf(saveCount, 6) + ".jpg";
      saveFrame(filename);
      lastCaptureTime = now;
      saveCount++;
    }
  }
}

