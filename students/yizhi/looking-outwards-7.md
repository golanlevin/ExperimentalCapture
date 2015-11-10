#Looking Outwards Report 7
## Rush Hour
####Liz Zhang

Below is an interesting video made by Fernando Livschitz, showing an ideal world where traffic is completely optimized by algorithms.
https://www.youtube.com/watch?v=MRPK1rBl_rI

The making of the video is explained in below video.
https://www.youtube.com/watch?v=S_doxRtYd8o

To summerize, the techniques of making this video include:
Shooting a video of a cross road and take multiple frames of cars in different times, then add artificial shaking on the final output images to make it look more authentic;
Pulling a matte (Rotoscoping) : The technique used here is a difference matte where it takes the difference of pixels in an image. In this case, the difference could be the shape of a car.
After that it's a simple matter of stitching everything on the same background and carefully add movement for them to be presented in the way shown in the video.

Thoughts of improvement:
Right now this process seems rather time consuming and very manual, but in computational photography there are already methods to do video synopsis automatically.
The automatic synopsis combines background subtraction, connected components analysis, and optimization.
I think it is interesting to implement video synopsis on the original video and see what comes of it.
