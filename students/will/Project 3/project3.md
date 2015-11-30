# Project 3 : Latent Environments
By Irene Alvarado & Will Miao

[![Walking to Sky slit scan](http://i.imgur.com/FyTC4g5.png)](https://vimeo.com/146692898 "Numbers")


## Concept
Our project was inspired by the corneal imaging work done by [Ko Nishino et al.](http://www1.cs.columbia.edu/CAVE/publications/pdfs/Nishino_IJCV06.pdf), whereby typically obscured information about an environment could be revealed and magnified through geometric transformations. We were motivated by uncovering the extra environmental information hidden within distorted reflections through a medley of techniques, outlined below.

![Cornea reflection](http://i.imgur.com/tnEi0Rb.png?1)


## Part 1 : Corneal reflection imaging
We began by experimenting with photographing corneal reflections and unwarping the images using the [VisualEyes software](http://www1.cs.columbia.edu/CAVE/software/visualeyes/), also by Ko NIshino et al. The unwarped images were strikingly clear and contained a considerable amount of information about the environment where it was taken.

![cornea](http://s27.postimg.org/68shbukrn/Screen_Shot_2015_11_23_at_5_53_19_PM.png)

![cornea unwarped](http://i.imgur.com/aGJV6zX.png)

We found that the photographer and her camera were permanent, exaggerated fixtures after unwarping the image, which we wished to minimize so as to capture more of the environment. To do this, we decided to use a [v360 360 degree camera](http://www.vsnmobil.com/products/v360), which has a smaller profile and wider resolution.


## Part 2 : Iris detection from live video feed
As we used the corneal imaging software to manually unwarp reflections one image at a time, we decided to try automating this process to apply this process not only on static images, but on videos as well. We began by testing existing eye detection libraries (ofxFaceTracker, ofxCv), but found that they primarily detect whole eyes and not irises specifically, which is what we were interested in. With some help from Golan, we implemented an ellipse fitting algorithm that uses RANSAC to automatically detect the iris. We were able to successfully get the algorithm detecting the edges of an eye, but not the iris. As you can see below, the algorithm was stuck detecting the contours of the eyelid:

![Automatic iris detection](http://cdn.makeagif.com/media/11-23-2015/TiAavq.gif)


## Part 3 : A second approach: Slit-scanning
Running into this wall with iris detection, we decided to take a different approach to creating the magnifying effect that we sought from corneal imaging: slit-scanning. Applied on still frames or video, this technique creates a temporal trail of information, which could be used to reveal certain features of an environment.  

We applied this technique on 360 degree video that we captured using the v360 camera. By playing with the position and width of the slit, as well as the scanning direction, we generated a variety of effects that elongate certain aspects of an image. 

[![Walking to Sky slit scan](http://i.imgur.com/WtSY7iX.jpg)](https://vimeo.com/146692819 "Walking to the sky")


## Processing Slit-scan code
```java
import processing.video.*;
Movie myMovie;

//  Capture myCap;
  int X=0;
  int i = 1;
  void setup() {
    
    //myCap = new Capture(this, 320, 240);
    //myCap.start();  
    size(1920, 800);
    myMovie = new Movie(this, "sky.mov");
    myMovie.loop();
    //myMovie.play();
    
  }
 
  void draw() {
    //image(myMovie,0,0);
    if (myMovie.available()) {
      myMovie.read();
      myMovie.loadPixels();
      frameRate(240);
      
	  //adjusting slit width, position, and scanning direction
	  //copy(myMovie, (myMovie.width/2), 0, 1, myMovie.height, (X++%width), 0, 1, height);
      //copy(myMovie, 0, myMovie.height/2, myMovie.width, 1, 0, (X++%height), width, 1);
      //copy(myMovie, 0, myMovie.height/2-40, myMovie.width, 40, 0, height-(X++%height), width, 40);
      copy(myMovie, 0, myMovie.height/2, myMovie.width, 1, 0, height-(X++%height), width, 1);
    }
  }
```
