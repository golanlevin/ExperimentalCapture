import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class magnifier extends PApplet {

PImage img1a;
PImage img1b;
PImage img2a;
PImage img2b;
PImage img3a;
PImage img3b;
PImage img4a;
PImage img4b;
PImage img5a;
PImage img5b;


public void setup()
{
 
  size(1350,600);
  background(255);
  smooth();
  img1a = loadImage("gym_DC.png"); //update with playground DC
  img1b = loadImage("gym_IR.png"); //update with playground IR
  img2a = loadImage("mag_DC.png"); //update with lego ?? 
  img2b = loadImage("mag_IR.png"); //update with ??
  img3a = loadImage("candle_DC.png");
  img3b = loadImage("candle_IR.png");
  img4a = loadImage("candle_zoom_DC.png");
  img4b = loadImage("candle_zoom_IR.png");
  img5a = loadImage("lego_DC.png");
  img5b = loadImage("lego_IR.png");
  
  frameRate(1);  
  
  image(img1a,25,100);
  image(img2a,250,100);
  image(img3a,475,100);
  image(img4a,900,100); 
  image(img5a,1125,100);
}


public void draw()
{

////  for(int i = 0; i < 1000; i++) {
//    
//  if(millis() - timer >= 3000) {
//     image(img1b,25,100);
//     image(img2b,250,100);
//     image(img3b,475,100);
//     image(img4b,900,100); 
//     image(img5b,1125,100);
//  
//  }  
//  else {
//     image(img1a,25,100);
//     image(img2a,250,100);
//     image(img3a,475,100);
//     image(img4a,900,100); 
//     image(img5a,1125,100);
//    }
//  }
//  
    if(frameCount%3 == 0){
     image(img1b,25,100);
     image(img2b,250,100);
     image(img3b,475,100);
     image(img4b,900,100); 
     image(img5b,1125,100);
    }
    else {
     image(img1a,25,100);
     image(img2a,250,100);
     image(img3a,475,100);
     image(img4a,900,100); 
     image(img5a,1125,100);
    }
  
}
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "magnifier" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
