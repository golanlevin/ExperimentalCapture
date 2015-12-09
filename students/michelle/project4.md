## Project 4: Projection Drawing
#### [Michelle Ma](../michelle/index.md)
-

![Turntable](https://github.com/michell3/Photos/blob/master/final/timeline.gif)
<br>
<br>
<img src="https://github.com/michell3/Photos/blob/master/final/composite.png" width="800">

-

#### Concept

This is the beginning of my investigation to combine stylized, hand-drawn portraits with the uncanny portraitures of photogrammetry. I used Agisoft Photoscan Pro to construct the mesh and project my images. The model displayed was created from 33 photos and 11 sketches.

The inspiration came from the fact that I love drawing portraits and capturing the essence of a person on paper. I wanted to combine it with photogrammetry, which is this imperfect way of capturing someone since the results are unmoving and uncanny. I wanted to see how my stylized rendering would counter that.

My process was to capture a person using my DSLR camera, feed it into photogrammetry software (Agisoft Photoscan Pro), and then replace some photo angles with my handdrawn portraits. I went through 3 photoshoots with 2 different people, but only one of the generated meshes was usable. This is because I could not capture all of the subject in the same instant, so my model was bound move. I cleaned up the mesh slightly in ZBrush, but there was still a significant loss of detail in important regions like the face.

The end result ended up being really interesting. I liked seeing my lines preserved on a 3D model. I was mostly disappointed in how musch detail was lost in the face because my interest in portraiture really comes from capturing a person's essence. I plan on keeping the investigation open to apply animated stylizations or other rendering effects. I also want to look into getting more cameras to remedy the issue with mismatched camera angles.

<br>
<img src="https://github.com/michell3/Photos/blob/master/final/screenshot.png" width="800">

-

#### Process

The technical challenges mostly originated from not having photos taken at the exact same moment, so I explored different methods to remedy the mesh situation. After that, texture generation was pretty straightforward in Photoscan and I drew the angles that were most clear in the final texture.

*Photography*
- Photograph a subject from at least 30 different angles, avoiding complex backgrounds and uneven lighting.

*Agisoft Photoscan Pro*
- Load in photos
- Filter inconsistent shots
- Align photos & build mesh
- Clean mesh (See ZBrush step)
- Filter photos for a cleaner texture
- Build texture
- Change the image paths to the drawn images (After the new renderings are finished)
- Build texture
- Export OBJ

*ZBrush*
- Import mesh and apply texture
- Dynamesh the model
- Smooth the mesh and add contours in areas like the face

*Photoshop & Drawing*
- Render the selected photos (Must have same dimensions and same position)

*Maya*
- Import model and texture
- Apply a surface shader with the texture
- Render image frames or export OBJ or DAE for OpenFrameworks

*OpenFrameworks*
- Use the ofxAssimpModelLoader addon for OpenFrameworks
- Import the OBJ/DAE
- Use the easyCam feature to view the model

-
#### Links
- [More Project Images](https://github.com/michell3/Photos/tree/master/final)
- [OpenFrameworks Source Code](../michelle/ModelViewer)

-
#### Special thanks to
- **Monisha Gopal** and **Sally McNichols** for being my subjects

<br>
<img src="https://github.com/michell3/Photos/blob/master/final/composite_actual.png" width="800">
