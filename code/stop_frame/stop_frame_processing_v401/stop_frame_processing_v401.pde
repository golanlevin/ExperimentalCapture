// TINY STOP-FRAME PROGRAM
// For Processing Version 4+.
// Saves an image from the camera whenever a key/mouse is pressed.
// Uses simple onion-skinning.
//
// Requires the "Video Library for Processing 4".
// To install this: Sketch->Import Library...->Manage Libraries...

//----------------------------------------------------------
// Parameters you can modify:
int videoWidth  = 1280;
int videoHeight = 720;
int whichCameraID = 0; 
int onionSkinTransparency = 127; // between 0 and 255

//----------------------------------------------------------
import  processing.video.*;
PImage  previousImage;
Capture myCapture;
int     saveCount = 0;
String  folderName;
boolean bDoSave = false;

//----------------------------------------------------------
void setup() {
  size(1280, 720);
  String[] cameras = Capture.list();
  printArray(cameras); // List the available cameras

  myCapture = new Capture(this, videoWidth, videoHeight, cameras[whichCameraID]);
  myCapture.start(); 
  folderName = year() + nf(month(),2) + nf(day(),2) + nf(hour(),2) + nf(minute(),2) + "/"; 
  previousImage = new PImage(myCapture.width, myCapture.height);
}

//----------------------------------------------------------
void keyPressed() {
  bDoSave = true;
}
void mousePressed() {
  bDoSave = true;
}

//----------------------------------------------------------
void draw() {
  if (myCapture.available()) {
    myCapture.read();

    if (bDoSave) {
      noTint();
      image(myCapture, 0, 0);
      String filename = folderName + "stopframe_" + nf(saveCount++, 5) + ".jpg";
      saveFrame(filename);
      bDoSave = false;

      previousImage.loadPixels();
      arrayCopy (myCapture.pixels, previousImage.pixels);
      previousImage.updatePixels();
      
    } else {
      noTint();
      image(previousImage, 0, 0, width, height);
      tint(255, 255, 255, onionSkinTransparency);
      image(myCapture, 0, 0, width, height);
    }
  }
}
