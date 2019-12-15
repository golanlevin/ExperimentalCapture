/*
 * Video Series to Vertical Slit Scans
 * Adapted from Golan's Example Code
 * http://www.flong.com/texts/lists/slit_scan/
 *
 * Michelle Ma 2015
 */
import processing.video.*;

// movie object data
Movie[] movies;
int movieIndex = 0;
boolean newFrame  = false;
// file data assuming same video dimensions and durations
String[] files = {"tina1", "tina2"};
float videoDur = 26;
int imgCounter = 0;

// slit scan variables
boolean isVertical = true;
int fRate = 1;
int drawX, drawY;

void setup(){
  // width and height of canvas are set to the video settings
  size(960, 540);
  background(0);
  
  // minimum frameRate for scanning completion
  if (isVertical) {
    fRate = max(ceil(height/videoDur)+1, fRate);
  } else {
     fRate = max(ceil(width/videoDur)+1, fRate);
  }
  frameRate(fRate);
  
  // initialization of movie objects
  movies = new Movie[files.length];
  for (int i = 0; i < files.length; i++) {
    movies[i] = new Movie(this, files[i] + ".mov");
    movies[i].frameRate(1);
  }
  
  println("Framerate at " + fRate);
  println("Starting " + files[movieIndex] + "...");
  movies[movieIndex].loop();
  
  // left-right slit scan
  drawX = 0;
  // bottom-up slit scan
  drawY = height - 1;
}

void draw() {
  if (isVertical) {
    verticalScan();
  } else {
    horizontalScan();
  } 
}

void horizontalScan() {
  if (newFrame) {
    loadPixels();
    for (int y = 0; y < height; y++) {
      int pixelIndex = y * width + drawX;
      if (pixelIndex >= pixels.length) {
        break;
      }
      pixels[pixelIndex] = movies[movieIndex].pixels[pixelIndex];
    }
    updatePixels();
    
    drawX += 1;
    newFrame = false;
    
    if (drawX > width) {
      reset();
    }
  }
}

void verticalScan() {
  if (newFrame) {
    loadPixels();
    for (int x = 0; x < width; x++) {
      int pixelIndex = drawY * width + x;
      if (pixelIndex >= pixels.length) {
        break;
      }
      pixels[pixelIndex] = movies[movieIndex].pixels[pixelIndex];
    }
    updatePixels();
    
    drawY -= 1;
    newFrame = false;
    
    if (drawY < 0) {
      reset();
    }
  }
}

// updates the frames of the movie file
void movieEvent(Movie m) {
  if (m == movies[movieIndex]) {
    m.read();
    newFrame = true;
  }
}

// called when a scan has finished processing
void reset() {
  movies[movieIndex].stop();
  String fileNum = nf(imgCounter, 2);
  save(files[movieIndex] + "_fr" + fRate + "_" + fileNum + ".png");
  imgCounter++;
  drawX = 1;
  drawY = height - 1;
  movieIndex++;
  
  if (movieIndex < movies.length) {
    println("Starting " + files[movieIndex] + "...");
    movies[movieIndex].loop();
  } else {
    println("Task completed");
    noLoop();
  }
}