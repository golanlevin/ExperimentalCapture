## Project 2: Synergy
#### Project Members: [Michelle Ma](../michelle/index.md), [Irene Alvarado](../irene/index.md), [Charlotte Stiles](../charlotte/index.md)
-
#### Project Video

[![IMAGE ALT TEXT](.-.)](https://vimeo.com/140160707 "Synergy")

-

#### Concept

My inspiration for this project came directly from [*Citius, Altius, Fortius*](https://vimeo.com/100576137) by Felix Deimann and [*Forms*](http://www.quayola.com/forms/) by Memo Atken and Quayola, who used Olympics footage to create some elegant, abstract animations. I wanted to make similar abstractions by using motion capture data and automating some of the animation using scripts in Maya. In addition, I wanted to work with two actors in order to create a collision of forces within the abstraction.

For the content of the animation, we had two actors who knew stage combat and two improv dancers. The first scene is a Judo scene, and I wanted to emphasize the mirrored movements of the actor by drawing shapes in between them. I went with a triangulated, paper look so that each frame would capture a sort of structure made by both of their bodies. The second scene is a sword fighting scene. The curves are the motion paths of the swords, and the spheres hint at the extremeties of each actor's limbs. The last scene is a dance scene that uses the same curve algorithm from the sword scene, but it is used to emphasize the parallels of the actors' movements.

The reason I called this project *Synergy* is because, halfway through my process, I was able to partner up with Irene and Charlotte for some Optitrack/Kinect action. The partnership was essential since we split up all the testing and capturing amongst the three of us. It was trully technical, but we are a capable team. In addition, working with actors and dancers was stupendous because of their positive attitude and the awareness they had of their own bodies.

<br>
<img src="https://github.com/michell3/Photos/blob/master/mocap/screen.jpg" width="415" height="295"> <img src="https://github.com/michell3/Photos/blob/master/mocap/sword_2.jpg" width="415" height="295">
<img src="https://github.com/michell3/Photos/blob/master/mocap/kinect.jpg" width="415" height="295"> <img src="https://github.com/michell3/Photos/blob/master/mocap/set.jpg" width="415" height="295">

-

#### Process

Our process had several steps involving Optitrack, Kinects, Maya, and etc. Here is a simplified breakdown.

*Optitrack*
- Activate the Optitrack system
- Suit up the actors
- Use 74 markers for 2 baseline skeletons
- Use 5-6 markers for 2 rigidbody swords
- Capture range of motion data for binding
- Export as FBX binary

*Kinects*
- Set up 3 Kinects (each with a laptop) on 3 sides of the subjects
- Set up light cameras and backdrop panels for cleaner capture data
- Record kinects, mocap, DSLR footage, and audio at the same times
- Export the data and combine them in Processing

*Generate Forms with Maya*
- Import FBX data with z-axis pointing up
- Triangulation
  * Create a triangular plane
  * Set each vertex to a joint
  * Create a deform cluster for each vertex
  * Constrain each cluster to its respective joint
  * Repeat
- Curves
  * Select a joint/locator
  * Use the [AnimToCurve](../michelle/Scripts/AnimToCurve) script
  * Use the [AutoPipe](../michelle/Scripts/AutoPipe) script with 'animation' and 'rebuild curve' selected
  * Use 'taper' feature
  * Rotoscope animation to timing

-
#### Links
- [More Project Images](https://github.com/michell3/Photos/tree/master/mocap)
- [Maya Scripts](../michelle/Scripts)

-
#### Special thanks to
- **Colin-James Whitney** and **Zachary Fifer** (left) for performing the fight scenes for us
- **Javier Spivey** and **...** (right) for dancing for us

<img src="https://github.com/michell3/Photos/blob/master/mocap/fighters.jpg" height ="550"> <img src="https://github.com/michell3/Photos/blob/master/mocap/dancers.jpg" height="550">