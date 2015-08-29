// TINY STOP-FRAME PROGRAM
// Saves an image from the camera when a key/mouse is pressed.
// For Processing Version 1.01.
 
//----------------------------------------------------------
// Parameters you can modify:
int videoWidth  = 320; // could be 160, 320, 640, etc.
int videoHeight = 240; // could be 120, 240, 480, etc.
int onionSkinTransparency = 127; // between 0 and 255
 
//----------------------------------------------------------
import  processing.video.*;
PImage  previousImage;
Capture myCapture;
int     saveCount = 0;
boolean bDoSave = false;
 
//----------------------------------------------------------
void setup(){
  myCapture = new Capture(this, videoWidth,videoHeight);
  myCapture.start();
  size(myCapture.width,myCapture.height);
  previousImage = new PImage(myCapture.width,myCapture.height);
}
 
//----------------------------------------------------------
void keyPressed(){
  bDoSave = true;
}
void mousePressed(){
  bDoSave = true;
}
 
//----------------------------------------------------------
void draw() {
  if(myCapture.available()) {
    myCapture.read();
 
    if (bDoSave){
      noTint();
      image(myCapture, 0,0); 
 
      String filename = "stopframe_" + nf(saveCount++, 5) + ".jpg";
      saveFrame(filename);
      bDoSave = false;
 
      previousImage.loadPixels();
      arrayCopy (myCapture.pixels, previousImage.pixels);
      previousImage.updatePixels();
    }
    else {
      noTint();
      image(previousImage, 0,0);
      tint(255, 255, 255, onionSkinTransparency);
      image(myCapture, 0,0);
    }
  }
}
