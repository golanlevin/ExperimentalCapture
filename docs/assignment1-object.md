# Project 1: Documentation of an Object

*Due Wednesday, September 23rd at the beginning of class.* 

--

Select one of the following two prompts: 

(A) ***[Lost Childhood Object](https://www.youtube.com/watch?v=QgHsYOybXa0)*** by Lenka Clayton:

[![Your Art Assignment: Lenka Clayton's Lost Childhood Object, 2015](http://img.youtube.com/vi/QgHsYOybXa0/0.jpg)](https://www.youtube.com/watch?v=QgHsYOybXa0)

or (B) ***[Embarrassing Object](https://www.youtube.com/watch?v=7mxM6mNSv5s)*** by Geof Oppenheimer:

[![Your Art Assignment: Geof Oppenheimer's Embarrassing Object, 2015](http://img.youtube.com/vi/7mxM6mNSv5s/0.jpg)](https://www.youtube.com/watch?v=7mxM6mNSv5s)

--

### Task

Using expanded capture techniques, realize the [lost/embarrassing] object virtually.  

--

### Requirements and Constraints

* Regardless of any intermediate processes or materials that your concept may or may not require (e.g. clay, papier-mache, etc.), your final project must be a virtual manifestation. Acceptable projects are limited to one of the following forms: 
	* a real-time software executable (created, for example, in Unity3D, openFrameworks, Processing, three.js, etc.) (Note: *interactivity* is optional).
	* a video or computer-generated animation 
	* a computer-generated rendering 
* Regardless of any subsequent digital transformations you might apply, you must "capture" "something" real (using a "device") as the initial basis for your virtual manifestation. 
* Your virtual object must be presented on a neutral background. 


#### Details 

* **Create** a Markdown document called <code>project1.md</code> in your student folder. You will document your project in this file. 
* In this document, **write** a couple of paragraphs (150-250 words) about the experience of creating the piece. Critique your work: where do you feel you succeeded? Where do you feel you fell short of what you'd hoped to achieve? What did you learn? 
* *All* projects must be documented with at least one digital image at least 1600 pixels wide. 
* With the exception of still renderings, *all* projects will be documented through online video hosted on YouTube or Vimeo, and linked from the <code>project1.md</code> page. (Note, Markdown does not allow video embedding, so use the technique [described here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#videos).) Software executables must be documented with a screencaptured video.
* Optionally, you are invited to publish 3D files to sharing/hosting sites such as [Thingiverse](http://www.thingiverse.com/thing:19276) or [Sketchfab](https://sketchfab.com/models/5bb11bc427eb49d7952fb857a1e3d98f).
* **Submit** your files (<code>project1.md</code>, various images, etc.) in the form of a pull request to this repository. 

-- 

#### What would be a "minimum viable project"? 

One example of a possible solution might be something like this: 

* Make a thing out of clay
* 3D scan it
* Bring it into Unity3D
* Add some sparkles, make it wiggle
* Record a screengrab video

Be more creative than that. 

-- 

#### References

A list of references and viewings is available [here](object-references.md). 

-- 

#### What Options do I have for Scanning Something? 

Hardware Options: 

* [3D Systems iSense 3D Scanner for iPad Mini Retina](http://cubify.com/info/tutorialssense)
* Kinect (v1 and v2)
	* [oF](https://github.com/micuat/ofxActiveScan)
	* [p5](https://github.com/ivaylopg/RGBDToolkit-to-Processing)
	* [Skanect (seems good for beginners)](http://skanect.occipital.com/)
	* [Kinect Fusion (pc)](https://www.youtube.com/watch?v=of6d7C_ZWwc	) [more info](https://msdn.microsoft.com/en-us/library/dn188670.aspx) 
       - Fast to process
		- Regular geometry
		- real time feedback
		- non cloud based
		- free tool
		- limited scale
		- does not work in sunlight
		- color is not very good
		- requires specific sensor with wall power
		- no texture map, per vertex color
		- [more on kinect fusion sdk](http://www.microsoft.com/en-us/kinectforwindows/develop/downloads-docs.aspx)
	* [DepthKit](http://depthkit.tv/)
		* [Depthkit js](https://vimeo.com/123520067)


* Matter and Form 3D Scanner

More difficult, but still available:

* [Pitt Orthopedics](http://www.engineering.pitt.edu/Sub-Sites/Labs/Orthopaedic_Robotics/Contact/)
* [Artec Space Spider] (https://www.youtube.com/watch?v=socspJqfkNE) (thanks to Yaser Sheikh) 3d scanner
* [School of Art 3d scanner at the DAS](http://www.cmu.edu/art/digital-arts-studio/3dscanning/index.html)

Software tools:

* [123D Catch ](http://www.123dapp.com/howto/catch) works with any regular camera, even your cell phone
	
	- works at any scale
	- works outside
	- generates a texture map
	- Photographic quality in color 
	- slow to process
	- cloud based
	- dense geometry
	- tools are not free and open
	- no real time feedback
	- more chaotic geometry 

* if you dont like 123D Catch - [Visual FSM & Meshlab] (http://www.instructables.com/id/Make-a-3D-model-from-pictures/?ALLSTEPS)
* [Agisoft photoscan (professional edition)](https://www.youtube.com/watch?v=DzCeHFEUaro)
  * [Tutorial from Specular](https://vimeo.com/specularprojects/photoscan1)
  * [part 2 of Specular tutorial](https://vimeo.com/specularprojects/photoscan2)


### After its Scanned What Can I Do?
(all of the following is from James George)

OBJ and PLY files are commonly used open 3D file formats.

The free tool MeshLab provides a very handy way to convert formats. It's like a 3D pocket knife. We'll be using it not just for converting 3D files to different formats, but also reducing and combining meshes. *see below for how to reduce meshes using a few other applications

[Here](https://www.youtube.com/playlist?list=PLBBF41579E4B65566) are some more comprehensive tutorials for cleaning geometry in MeshLab


After capturing your geo, the following links will help you get it into your preferred application

* [Unity3d](https://unity3d.com/)
Supports OBJ like any other 3D file format!

* Processing
The Saito OBJ loader
[Processing Library](https://code.google.com/p/saitoobjloader/)
[Tutorial Video]( https://www.youtube.com/watch?v=6VSaneuiaWs) (scrub to 3:30 for the good stuff)

* OpenFrameworks
The ofMesh and ofVboMesh objects support PLY's with color with the mesh .load() function. This is what you saw in class.
	* The built in addon ofxAssimpModelLoader also works on OBJ files

* [Satoru HIga has a nice OBJ loader addon:]
(https://github.com/satoruhiga/ofxObjLoader)

* Cinder
   * [Cinder has built in support for OBJ]
(http://libcinder.org/docs/v0.8.3/classcinder_1_1_obj_loader.html)

    * [There is also a Mesh extension block that supports PLY] (https://github.com/simongeilfus/Cinder-OpenMesh)
    * [Meshes in cinder tutorial] (http://www.creativeapplications.net/tutorials/guide-to-meshes-in-cinder-cinder-tutorials/)

* 3D Printing
	* NetFabb will help you clean up models if you wish to 3D print them. You'll want to take them through the STL format in MeshLab
[http://www.netfabb.com/downloadcenter.php?basic=1](http://www.netfabb.com/downloadcenter.php?basic=1)

Creative Tools:
Many applications support OBJ (and sometimes PLY files)

* Photoshop (really!)
Photoshop natively supports importing and painting on 3D files! Check out [this tutorial](https://www.youtube.com/watch?v=mD39wgDoiHE)

* After Effects
The 3D Animator Pro plugin (they offer a free trial) accepts OBJ files [video ](https://www.youtube.com/watch?v=eEQUba16V5o)

* Plexus is an amazing tool for After Effects that works on 3D geometry [video](https://www.youtube.com/watch?v=44hz_fsjX7o)

* There is also mesh reduction tutorial for the free program Blender [video]
(https://www.youtube.com/watch?v=ttU6Gz1W0Xw)

Programs like Maya, Cinema4D, Houdini, 3D Studio Max, Modo also work well with OBJ files but are beyond the scope of what we expect to teach in this class. But if you know these programs, by all means use them for your portraits.

--------------------------

Alignment

* [Meshlab 3D Scanning: Alignment] (http://youtu.be/4g9Hap4rX0k)
* [Alignment and Registration in CloudCompare] (http://www.danielgm.net/cc/doc/wiki/index.php5?title=Alignment_and_Registration )
   * I've found that CloudCompare is really good for loading large pointclouds or found research data in lasercanning formats like .las, .xyz etc. and it will do a great job with Kinect or photogrammetry pointclouds. 

Reduction & Remeshing

* Poisson Reconstruction in Meshlab - This is a good general purpose approach for Kinect or other pointclouds. Can also be used to combine meshes when used after "flatten visible layers" in Meshlab. 

Color

 * [MeshLab Features: Vertex Attribute Transfer](
http://youtu.be/sKKmJdsk7Tg?list=UU70CKZQPj_ZAJ0Osrm6TyTg)




