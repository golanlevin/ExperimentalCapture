// TINY TIME-LAPSE + STOP-FRAME PROGRAM
// by Golan Levin, June 2019
//
// Captures a frame from the webcam once per second,
// or at some other user-defined interval, or 
// when the user presses the spacebar, and
// saves the result to a file on the OSX Desktop.
//
// Known to work with Processing Version 3.5.3+.
// You'll need to install the Processing Video library, 
// and the Video Export library for Processing by Abe Pazos.
// Go: Sketch > Import Library... > Add Library...
//
// You'll also need to install ffmpeg for the video export. 
// See http://ffmpeg.org/. 


//----------------------------------------------------------
import  processing.video.*;
import  com.hamoid.*;

Capture     myCameraCapture;
VideoExport videoExporter;
long        lastCaptureTime = 0;
int         saveCount = 0; 

boolean     frameCaptureCondition = false; 
int         MODE_STOP_FRAME = 0; 
int         MODE_TIME_LAPSE = 1; 

//----------------------------------------------------------
// Parameters you can modify
int videoWidth  = 1280; // could be 160, 320, 640, 1280, etc.
int videoHeight = 720;  // could be 120, 240, 480, 720, etc.
int      period = 1000; // milliseconds between webcam frames
int whichCamera = 0; 
int mode = MODE_STOP_FRAME; 

String username = "studioadmin";
String savePath = "/Users/"+ username + "/Desktop/"; // Where to save the result


//----------------------------------------------------------
void setup() {
  size(1280, 720);

  String[] cameras = Capture.list();

  if (cameras == null) {
    println("Failed to retrieve the list of available cameras, will try the default...");
    myCameraCapture = new Capture(this, videoWidth, videoHeight);
  } else {

    printArray(cameras);
    myCameraCapture = new Capture(this, 1280, 720, cameras[whichCamera]);
  }
  myCameraCapture.start(); 

  String saveTime = year() + nf(month(), 2) + nf(day(), 2) + nf(hour(), 2) + nf(minute(), 2); 
  String saveType = (mode == MODE_TIME_LAPSE) ? "timelapse_" : "stopframe_";
  String timelapseFilename = savePath + saveType + saveTime + ".mp4"; 
  videoExporter = new VideoExport(this, timelapseFilename, myCameraCapture);
  videoExporter.startMovie();
}

//----------------------------------------------------------
void draw() {

  // If there's a fresh frame, read and draw the camera image.
  if (myCameraCapture.available()) {
    myCameraCapture.read();
    image(myCameraCapture, 0, 0); 

    if (mode == MODE_TIME_LAPSE) {
      long now = millis();
      if ((now - lastCaptureTime) >= period) {
        frameCaptureCondition = true; 
        lastCaptureTime = now;
      }
    } 

    // Check if it's time to add a new frame to the video. 
    if (frameCaptureCondition) {
      videoExporter.saveFrame();
      frameCaptureCondition = false; 
      saveCount++;
    }
  }
}

//----------------------------------------------------------
void keyPressed() {
  // if quit or escape, save the video. 
  if ((key == 'q') || (key == 'Q') || ((int)key == 27)) { 
    videoExporter.endMovie();
    println("Saved movie with " + saveCount + " frames"); 
    exit();
    ;
  } else if ((key == ' ') && (mode == MODE_STOP_FRAME)) {
    frameCaptureCondition = true;
  }
}
