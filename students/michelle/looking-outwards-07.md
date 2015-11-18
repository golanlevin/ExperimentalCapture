
## Looking Outwards 07

### Stylized Hair Capture
#### Disney Research Zurich and Universidad de Zaragoza
--
#### Project Video
[![Project Video](http://2.bp.blogspot.com/-PU0IHQrdXDY/U_W8vsgAicI/AAAAAAAAATM/DXgqPlEhCns/s1600/capturing_and_stylizing_hair_for_3d_fabrication_by_cheve-d7w1a3e.jpg)](https://www.youtube.com/watch?v=QRBkdhZwBic)
--
This research attempts to create a method in which hair styles can be captured and reproduced. The research was spurred on by the technological developments in capturing human traits and was inspired by sculptural renditions of hair. Their methods in a nutshell are to retrieve a smooth surface representation of the hairstyle and then introduce a novel color stylization operator to be applied over the mesh domain. The color stylization process involves initializing the color, stylizing the color, and then stylizing the mesh from the color.

For the data acquisition step, they only use 4 perspective shots from a DSLR camera and use a multi-view stereo reconstruction algorithm to compute partial reconstructions from the four orientations. These are then aligned using the Iterative Closest Points algorithm, and then the hair is hand-masked for processing. The color stylization is then produced through methods of directional smoothing and orthogonal shock filters. After that, the geometry is revisited and uses the high contrast regions in the hair colorization to create "wisp profiles" that reflect the stylized texture used in sculptural approaches to hair.

The high quality busts produced from this research are really promising. I'm especially impressed they only needed 4 different perspectives for capture. I can see this being extended in other types of capture for objects that are appear in large groups but are stylistically replesented as clumps of a certain texture. For example, when capturing a tree, you can't capture every single leaf, so you need a way of representing it's groupings. Some of the downsides to this project are its reliance on color. I don't know how this method fairs with black hair or afro hair. This could possibly be fixed by integrating alternate lighting methods but that might contradict the simplicity of the capture.

--

[Research Paper](http://www.disneyresearch.com/wp-content/uploads/Project_StylizedHairCaptureSIGGRAPH14_paper1.pdf)

[Project Website](http://www.disneyresearch.com/publication/stylized-hair-capture/)

![More Hair](http://3dprintingindustry.com/wp-content/uploads/2014/08/facialhair-3d-scanning.png)

![Hair Gif](http://www.technoviser.com/wp-content/uploads/2014/08/disney-research-latest-tech-will-accurately-3d-print-stylized-hair.gif)

![Hair](http://www.tctmagazine.com/downloads/5061/download/Project_StylizedHairCaptureSIGGRAPH14_teaser%20(1).png?cb=9d0699e0a187e1052a56acf167f4565d)
