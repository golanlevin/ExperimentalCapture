####Project 2
## A Person in Time - An Application of Eulerian Video Magnification on 3D Portrait
####Liz Zhang

###The idea
Eulerian Video Magnification is a technique to visualize subtle changes of color or movement in videos by magnifying signals of a chosen frequency. This technique was first proposed in the paper [Eulerian Video Magnification for Revealing Subtle Changes in the World](http://people.csail.mit.edu/mrub/papers/vidmag.pdf)
Former application of Eulerian Video Magnification can be found here:
[![IMAGE ALT TEXT HERE](https://cloud.githubusercontent.com/assets/11666005/10568605/7cfe19c6-75e8-11e5-9fcf-8ac49cb73da9.png)](https://www.youtube.com/watch?v=e9ASH8IBJ2U)

In this project I captured a 3D video of a person and added wrapping motion to it at the the same attitude and frequency as the person’s heart rate.
![](https://cloud.githubusercontent.com/assets/11666005/10568697/d8eac224-75e9-11e5-980e-4b32a667c436.png)

###Tools
The tools used for this project are a DepthKit (a DSLR camera and a Kinect). The DSLR is calibrated with the Kinect to obtain the  RGBD data. 

###Process
Video capture
2.   Eulerian Video Magnification
The video captured by the DSLR is processed with the method described in the Eulerian Video Magnification. The frequency range of 70 to 95Hz single is extracted and amplified. However instead of visualizing the amplified result as color change directly in the video, I extract the signal by choosing the mean of human face area in I channel (of the HIV color space). Did some more frequency cleaning to obtain the approximate signal changing pattern. Shown as below:
![](https://cloud.githubusercontent.com/assets/11666005/10568181/84eeba06-75e2-11e5-953d-1cb39851cfa8.jpg)
![](https://cloud.githubusercontent.com/assets/11666005/10568182/878b3866-75e2-11e5-9b60-bfb3a5e20cfa.jpg)

This signal was then parsed to an xml file to substitute XSinAmpt.xml. 
![](https://cloud.githubusercontent.com/assets/11666005/10568200/b9aaf336-75e2-11e5-844f-55e01ec3f6e1.png)
This file was then used to generate the wrap motion using DepthKit visualization.
![](https://cloud.githubusercontent.com/assets/11666005/10568180/803b391c-75e2-11e5-9776-59c50fcc44d2.png)

###Final result
The final result is shown in the video below. Click for viewing:
[![IMAGE ALT TEXT HERE](https://cloud.githubusercontent.com/assets/11666005/10592898/4510c8ce-768d-11e5-9647-7b3d7dd86a58.png)](https://youtu.be/4G-CQoTlcdE)

[![IMAGE ALT TEXT HERE](https://cloud.githubusercontent.com/assets/11666005/10568319/5895413a-75e4-11e5-9c8f-558b2ffd2258.png)](https://www.youtube.com/watch?v=letdB7cHY-g)

###Reference
1. Wu, Hao-Yu, et al. "Eulerian video magnification for revealing subtle changes in the world." ACM Trans. Graph. 31.4 (2012): 65.

2. https://github.com/obviousjim/DepthKit
