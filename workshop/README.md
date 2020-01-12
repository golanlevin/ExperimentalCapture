# Experimental Capture Workshop

### Computational & Expanded ███ography, <br/>Anderson Ranch, August 2018

***NOTE: Documents have moved; links below may be outdated.***

[Golan Levin](http://flong.com) / [@golan](http://twitter.com/golan) <br />
A one-week workshop taught at Anderson Ranch, July 2016<br />
For complete info, see the [**Experimental Capture main page**](../README.md). 

--
### Learning Objectives

This workshop introduces some experimental media practices that arise from using devices to "capture" the world. In particular, we are concerned with how we can understand and build representations of the world using devices that sense beyond the limits of human perception. 

---

## Monday

1. Introduction. Meet & Greet; Discussion & Objectives 
	* Tomography and [Holes in Swiss Cheese](https://www.nytimes.com/2015/05/29/world/europe/switzerland-scientists-find-the-secret-to-the-holes-in-swiss-cheese-hay-dust.html); "Mechanism and control of the eye formation in cheese" [paper](https://scinapse.io/papers/2024396341), [paper](https://link.springer.com/article/10.1007/s13594-012-0105-2), e.g. ["There is demand for non‐destructive monitoring of eye formation in cheese during ripening."](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1471-0307.2009.00478.x), [[PDF](../docs/pdf/eye-formation-in-cheese.pdf)]
![Eyes in cheese](../docs/images/cheese.gif)
	
1. A quick, incomplete list of some hands-on stuff we'll cover: 
	* 3D scanning and Photogrammetry 
	* Multi-spectral imaging (NIR, UV, Thermal)
	* High-speed videography and other temporal play
	* 360-degree video 
	* Gesture capture & OSC
	* Binaural & ultrasonic audio
	
1. Appetizers
	* [What is a Camera? Conceptual Cameras](../docs/conceptual-cameras.md)
	* [Perspective Capture and Representation](../docs/perspective.md)

#### Main Topics: *Multi-spectral* and *High-speed* imaging.

Today's topic is seeing beyond human perception, with: **Multi-spectral imaging** (NIR, UV, Thermal) and **High-speed videography**. Lectures include:  
* [Multispectral & Hyperspectral Imaging](../docs/hyperspectral.md)
* [Overcranking (Slow-Motion/Hi-Speed)](../docs/overcranking.md)

#### Activities and Exercises

1. Demonstrations of UV, IR, Thermal (FLIR & Axis) imaging. Also: Thermochromic, phosphorescent, retroreflective, and polarizing sheets and surfaces.
1. Demonstrations of the Edgertronic high speed camera. Here's the Edgertronic [Beginner's Guide to High-Speed Video](http://wiki.edgertronic.com/index.php/Beginner's_Guide_to_High_Speed_Video), and their [Quick Start Guide](https://wiki.edgertronic.com/index.php/Quick_start_guide), which may be helpful if you want to know more. 

#### Auxiliary/Secondary Topic: *Audio*

* [Binaural recording](../docs/audio.md)
* [Ultrasonic recording]()

---

## Tuesday

#### Into 3D: Viewings

* Depth from stereo, 1930s-style: The [Stereoplotter](https://en.wikipedia.org/wiki/Stereoplotter)
* [A brief history of photogrammetry](../docs/Photogrammetry-and-3D-scanning.md)
* [James George at Eyeo2015](https://vimeo.com/134973504) (view from 7:34, "Camera of the Future") and on [Medium](https://medium.com/@obviousjim/spatialstorytelling-fa4b6ace3e16)
* [James George & Jonathan Minard, *CLOUDS*](http://cloudsdocumentary.com/)


#### 3D capture technologies: 

* [EinScan Pro+ 3D](https://www.einscan.com/einscan-pro-plus?) scanner
* Intel RealSense & [DepthKit](http://www.depthkit.tv/)
* AgiSoft PhotoScan
	* Alex Porter's Photoscan Tutorial #1: [Capturing with Photoscan](https://vimeo.com/123701711)
	* *Optional viewing*: Alex Porter's Tutorial for [Cleaning Photoscans](https://vimeo.com/123702711)
	* [Michelle's tutorial](https://github.com/golanlevin/ExperimentalCapture/blob/master/students/michelle/tutorial2.md) for using PhotoScan
	* [Claire's tutorial](pdf/photogrammetry_from_video_with_photoscan.pdf) for PhotoScan from video frames
	

#### Concepts in Portraiture: 

* [Portraiture in time](https://github.com/golanlevin/ExperimentalCapture/blob/master/docs/event.md#people)
* [Portraiture](../docs/portraits.md)
* [Portraiture (continued)](../docs/portraits_2.md)

#### Auxiliary/Secondary Topic: *Time Play*

* [Moving Cameras (shutter stroboscopy)](../docs/moving-cameras.md)
* [Undercranking and Time Lapse](../docs/undercranking.md)
* [Slit-Scanning](http://www.flong.com/texts/lists/slit_scan/)

#### Topic: 360° Capture

* [Panoramic, 360-degree, and environmental capture](../docs/environmental-capture.md)
* Smokey Dyar's thesis on 360 filmmaking, [Stuck in Spheres](http://stuckinspheres.com/)
* Jessica Brillhart's [Google lecture on 360° filmmaking](https://www.youtube.com/watch?v=t3xDgONMdlM)
* Michael Naimark's writeup of [360° cinematography studies](https://medium.com/@michaelnaimark/vr-cinematography-studies-for-google-8a2681317b3)


---

## Wednesday

#### Concepts in Capture

* [Capturing and Representing Objects: Still Life & More](../docs/object-references.md)
* [Gesture recording and playback; 2D & 3D motion capture](../docs/gesture.md)
* [Events](../docs/event.md)

#### Mini Technical Lectures:

* Computing a [depth map from stereo images](https://github.com/CreativeInquiry/stereobm_depth_map), [download binary](download/stereobm_depth_map.zip)
* [Gonioreflectometry](../docs/gonioreflectometry.md) 
* [Long Exposure and Light Painting](../docs/longexposure.md)
* [Bullet Time (Array Videography)](../docs/bullettime.md)
* Backwards (Retrograde) Time](../docs/backwards.md)
* [Looping (Canon) Time](../docs/looping.md)


#### Activities and Exercises

Demonstrations of OSC: 

* [BlinkOSC](../code/osc/blinkOSC.zip)
* [EyeOSC](../code/osc/EyeOSC.zip)
* [FaceOSC](../code/osc/FaceOSC.zip) / [video](https://vimeo.com/26098366) / [Templates](https://github.com/CreativeInquiry/FaceOSC-Templates)
* [GyrOSC](../code/osc/gyrOSC.zip)
* [TouchOSC](../code/osc/touchOSC.zip)

Additional controllers: 

* [LEAP controller](https://github.com/nok/leap-motion-processing), [ManosOSC](https://github.com/n1ckfg/ManosOsc)
* [3D SpaceNavigator] (https://gist.github.com/brysonian/100144)
* Scanse LIDAR
* [Sensel Morph](../code/ofxSenselMorph2.zip)




---

<!---

	


---

### Thursday 

1. Mini Lectures
	* 
	* [Slit Scanning](http://www.flong.com/texts/lists/slit_scan/)
	* [Expanded Audio Capture](../docs/audio.md)

-- 

### Beyond


*To be organized on-the-fly, responding to circumstances. A list of activities and lectures we'll draw from throughout the week:*



* [Pixillation and Stop-Frame](../docs/pixillation.md)
* [Backwards (Retrograde) Time](../docs/backwards.md)
* [Looping (Canon) Time](../docs/looping.md)
* *[Portraiture: Capturing People and Movements](../docs/portraits.md)*
* *[Landscape: Capturing Places](../docs/places.md)*

--->
