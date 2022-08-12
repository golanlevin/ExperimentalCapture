// Simple slit-scanning program. 
// Works with Processing 4.0.1.
// Golan Levin, 2022

import processing.video.*;
Capture cam;
int dstX = 0;

void setup() {
  cam = new Capture(this, 640, 480, 30);
  cam.start();  
  size(640, 960);
}

void draw() {
  // Set some parameters for capture and display.
  int srcX = (mousePressed) ? mouseX : cam.width/2; 
  int srcY = 0; 
  int srcW = 2; // how wide is the stripe?
  int srcH = cam.height; 
  int dstY = cam.height; 
  int dstW = srcW; 
  int dstH = srcH; 
  
  // Draw the camera feed, and the source stripe indicator
  image(cam, 0, 0, cam.width, cam.height);
  stroke(255, 80); 
  strokeWeight(5); 
  line(srcX, srcY, srcX, srcY+srcH); 

  // If there's fresh camera data, 
  // copy the stripe of pixels to the screen,
  // and advance the drawing destination. 
  if (cam.available()) {
    cam.read();
    cam.loadPixels();
    copy(cam, srcX, srcY, srcW, srcH, dstX, dstY, dstW, dstH);
    dstX = (dstX+srcW)%width;
  }
}
