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

![Hypercentric lens](data:image/jpeg;base64,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)
 
![Hypercentric lens](http://www.opto-engineering.kr/media/timthumb.php?src=pc/sample_01.jpg&w=800)

-- 

### Perspective Correction

![ofxCorrectPerspective](images/ofxcorrectperspective.jpg)<br />

#### ofxCorrectPerspective 

* [ofxCorrectPerspective](https://vimeo.com/95204456) on Vimeo
* [ofxCorrectPerspective](https://github.com/harisusmani/ofxCorrectPerspective) on GitHub

**[ofxCorrectPerspective](http://golancourses.net/2014/haris/05/14/capstone/)** by CMU student Haris Usmani is an OpenFrameworks add-on that performs automatic 2d rectification of images. It’s based on work done in “Shape from Angle Regularity” by Zaheer et al., ECCV 2012. Unlike previous methods of perspective correction, it does not require any user input (provided the image has EXIF data). Instead, it relies on the geometric constraint of ‘angle regularity’ where we leverage the fact that man-made designs are dominated by the 90 degree angle. It solves for the camera tilt and pan that maximizes the number of right angles, resulting in the fronto-parallel view of the most dominant plane in the image.
