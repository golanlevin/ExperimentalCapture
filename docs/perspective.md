# Perspective Capture and Imaging

### Perspective Representation

Size = Proximity. (Right?)

![Forced perspective by mtsonic](images/forced-perspective.jpg)<br />
*Forced perspective by [mtsonic](https://www.flickr.com/photos/mtsonic/2933383930/).*

Owing to our familiarity with perspective imaging, we take for granted that things which are larger, are closer. (When we play with this notion, it's called [*forced perspective*](http://naldzgraphics.net/photography/forced-perspective-photos/).) But it wasn't always this way, and it doesn't have to be. 

### Hierarchical size 

Size = Importance.

![Hierarchical proportion in Egyptian art](images/hierarchical-proportion.jpg)<br />
*At left, from [here](http://www.curatorscorner.com/2014_10_01_archive.html?m=1): "Senwosret-senebefny, an Egyptian official in the Twelfth Dynasty (1937–1759 bce), depict the deceased squatting on the ground covered in a cloak. The small figure is Itneferuseneb, most likely Senwosret-senebefny’s wife." At right: Family Group, mortuary statue, ca 2371–2298 bce.*

This is *psychological* rather than *mechanical* representation.

![A child's drawing](images/child-drawing.jpg)

### Perspectiveless Imaging

Size = A Question of Composition

The "lack" of perspective is a common feature in Asian, Indian, and Medieval European art. Notice how the characters are all the same size, even if they are further away. Well, "further away" from what? Who (or what) is the implied observer here? 

![Hierarchical proportion in Egyptian art](images/akbar-flat-perspective.jpg)<br />
*[Akbar Inspecting the Construction of Fatehpur-Sikri](http://www-personal.umich.edu/~pomorski/mug1.html)*, Mughal empire, India (c. 1590).

It's important to remember that *perspective is an invented technology for representing the 3D world in two dimensions*. It was invented in 1435, by Leon Battista Alberti (1404-1472), who provided the first theory of what we now call linear perspective in his book, *On Painting.* After 1435, the technology spread rapidly throughout Europe. 

![Before and after the invention of perspective](images/perspective.jpg)<br />
*The Last Supper*, by Ugolino De Nerio (circa 1325), and Leonardo Da Vinci (circa 1494).

### Orthographic/Isometric and Other Projections 

Orthographic projection is an alternative to perspective projection, in which parallel lines don't converge. It is widely used in engineering drawings, for dimensioning parts. 

![Orthographic projection](images/orthographic.jpg)

Orthographic projection has been known since antiquity; [according to Wikipedia](https://en.wikipedia.org/wiki/Orthographic_projection#Origin), Hipparchus used the projection in the 2nd century BC to determine the places of star-rise and star-set. In about 14 BC, Roman engineer Marcus Vitruvius Pollio used the projection to construct sundials and to compute sun positions.

Here is Hans Lencker's "Machine for Orthographic Projection" in 1571. You can think of this as an *orthographic camera*. 

![Hans Lencker's "Machine for Orthographic Projection"](https://drawingmachines.org/images/machine/17/web/1571_HansLencker_Machine_for_Orthographic_Projection_DETAIL_MachineOnly.jpg)<br />
*Hans Lencker's "Machine for Orthographic Projection" (1571), from [DrawingMachines.org](https://drawingmachines.org)*

![Alfred Molteni's Cranial Tracing Device, circa 1860]
(https://drawingmachines.org/images/machine/193/web/1860-62_AlfredMolteni_CranialTracingDevice_by_Broca.jpg)<br />
*Alfred Molteni's Cranial Tracing Device, circa 1860, from [DrawingMachines.org](https://drawingmachines.org)*


Furthermore, just because you have 3D-dimensional data in a computer, it doesn't mean that it must be rendered with perspective projection. *Perspective projection is simply the default rendering mode in OpenGL and DirectX.* 

![Orthographic perspective in *Gangster Squad*](images/isometric_environment.jpg)<br />
Orthographic perspective in *Gangster Squad*.

In fact, there are a wide variety of alternative graphical projection methods, including orthographic () mode, above (also called isometric or "ortho"), and more. (For orthographic projection in openFrameworks, see [ofCamera](http://openframeworks.cc/documentation/3d/ofCamera.html) and [ofEnableOrtho()](http://openframeworks.cc/documentation/3d/ofCamera.html#show_enableOrtho).) Are you using linear perspective in your interactive VR? Ask yourself if you're just being *lazy*. 

![Alternative graphical projection methods](https://upload.wikimedia.org/wikipedia/commons/4/41/Graphical_projection_comparison.png)<br />
*Alternative graphical projection methods.*

-- 

### Telecentric Lenses

A [*telecentric lens*](https://en.wikipedia.org/wiki/Telecentric_lens) is an unusual type of lens whose focal point is at infinity. It naturally produces an orthographic view of its subject. 

![Telecentric imaging, from Edmund Optics](images/telecentric.gif)<br />
*Telecentric imaging, from Edmund Optics.*

![Telecentric imaging, from Edmund Optics](images/telecentric-photo.jpg)<br />
*Illusion picture made with a digital camera and a telecentric lens system, [from here](http://www.lhup.edu/~dsimanek/3d/telecent.htm).*

-- 

### Hypercentric and Pericentric Lenses

A hypercentric lens provides a converging view of an object, letting you see the top and all around the sides, simultaneously.

![Hypercentric lens](https://cloud.githubusercontent.com/assets/290053/10875019/a45dbe04-80fb-11e5-913b-9d0123b759c4.jpg)
 
![Hypercentric lens](http://www.opto-engineering.kr/media/timthumb.php?src=pc/sample_01.jpg&w=800)

-- 

### Perspective Correction

![ofxCorrectPerspective](images/ofxcorrectperspective.jpg)<br />

#### ofxCorrectPerspective 

* [ofxCorrectPerspective](https://vimeo.com/95204456) on Vimeo
* [ofxCorrectPerspective](https://github.com/harisusmani/ofxCorrectPerspective) on GitHub

**[ofxCorrectPerspective](http://golancourses.net/2014/haris/05/14/capstone/)** by CMU student Haris Usmani is an OpenFrameworks add-on that performs automatic 2d rectification of images. It’s based on work done in “Shape from Angle Regularity” by Zaheer et al., ECCV 2012. Unlike previous methods of perspective correction, it does not require any user input (provided the image has EXIF data). Instead, it relies on the geometric constraint of ‘angle regularity’ where we leverage the fact that man-made designs are dominated by the 90 degree angle. It solves for the camera tilt and pan that maximizes the number of right angles, resulting in the fronto-parallel view of the most dominant plane in the image.
