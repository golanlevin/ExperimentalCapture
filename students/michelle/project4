## Project 4: Projection Drawing
#### [Michelle Ma](../michelle/index.md)
-
#### Project Video

[![IMAGE ALT TEXT](https://github.com/michell3/Photos/blob/master/projection/cover.png)](https://vimeo.com/michell3 "Projection Drawing")
![Composite Preview](https://github.com/michell3/Photos/blob/master/projection/composite.png)

-

#### Concept

My original idea for this project was to combine slitscanning with photogrammetry in order to create surreal portraits reminiscent of Salvador Dali's landscapes. My sources of exploration came from [Golan's Informal Catalogue of Slit-Scan Video Artworks and Research](http://www.flong.com/texts/lists/slit_scan/) and [Memo Atkin's Volumetric Slitscanning Examples](http://www.memo.tv/volumetric-slitscanning/).

I invited several of my friends to the Kinoptic Dome in order to capture their movements for intervals of 3-5 seconds. Ideally, I would have liked to use the panoptic dome for the video data. However, those resources were not available to me so I switched gears to point cloud data. Keep in mind that there was 80GB of point cloud data for 5 scenes, each being 3-5 seconds long. The point clouds ended up being 650K - 700K points each. In addition, I really struggled with finding the right software to handle the data but finally settled with OpenFrameworks and MeshLab to convert the point clouds into meshed OBJs. After that, writing the program to manipulate the point cloud data was fun and fluid to write!

The mesh data actually is not very strong from these kinects, so the results have more of a glitch aesthetic. I am more drawn to the point cloud screen shots from the OpenFrameworks viewer.

![Mesh Objects](https://github.com/michell3/Photos/blob/master/slitscan/mesh_previews.png)

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
- Use the easycam feature to view the model

-
#### Links
- [More Project Images](https://github.com/michell3/Photos/tree/master/projection)
- [OpenFrameworks Source Code](../michelle/ProjectionDrawing)

-
#### Special thanks to
- **Monisha Gopal** and **Sally McNichols** for being my subjects
