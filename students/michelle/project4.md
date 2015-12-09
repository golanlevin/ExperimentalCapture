## Project 4: Projection Drawing
#### [Michelle Ma](../michelle/index.md)
-

![Turntable](https://github.com/michell3/Photos/blob/master/final/timeline.gif)
<br>
<br>
<img src="https://github.com/michell3/Photos/blob/master/final/composite.png" width="800">

-

#### Concept

This idea was prompted by the Person in Time projects and by my interest in drawing portraits and the human figure. When I was but a wee budding artist in high school, I always got random requests to draw portraits--even if I didn't know the person. I drew people for fun at first but then I became disturbed at how they wanted me to replicate their Facebook profiles, or invest a lot of time into a small superficial gift. However, I still enjoy drawing people. In fact, whenever I see a person with interesting and distinct facial features, I'm always itching to draw him/her in the most natural way possible. When I had more time on my hands, I would go people watching and practice captureing the essence of a person on paper.

So when I heard that we were supposed to capture a person, I really wanted to return to my portrait drawing origins. I decided to combine it with Photogrammetry because capturing people in 3D is quite popular but incredibly weird to me since the results are on the deeper end of the uncanny valley. I wanted to see if my rendering style could either counteract the strangeness in order to make a 3D portrait.

My process was to capture a person using my DSLR camera. I went through 3 trials with 2 different people, and the results were not very promising since the photos technically cannot line up at the same instant if the person shifts even a little bit. I finally was able to generate a relatively clean model on the third try, but still had to clean the mesh in ZBrush. Adter that, I experimented with selecting the photos that were going to be projected onto the mesh, and then replicated them in my drawings. (No, I did not trace the photos, I just referenced them, which doubly contributed to some mismatched lines.)

The end result ended up being really interesting. I liked seeing my lines preserved on a 3D model. I was mostly disappointed in how musch detail was lost in the face because my interest in portraiture really comes from capturing the fine features of someone's face. If I could do the project again, I would have multiple cameras to capture a person at every angle. However, those resources aren't currently available to me, so this remains an experiment in projecting drawings onto a 3D model.

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
