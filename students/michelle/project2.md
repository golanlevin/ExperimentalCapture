## Project 2: Synergy
#### Project Members: [Michelle Ma](../michelle/index.md), [Irene Alvarado](../irene/index.md), [Charlotte Stiles](../charlotte/index.md)
-
#### Project Video

[![IMAGE ALT TEXT](https://github.com/michell3/Photos/blob/master/mocap/swords_v2_0907.png)](https://vimeo.com/143089691 "Synergy")

<img src="https://github.com/michell3/Photos/blob/master/mocap/judo_render_2_0259.png" width="426"> <img src="https://github.com/michell3/Photos/blob/master/mocap/swords_v2_0352.png" width="426">

-

#### Concept

My inspiration for this project came directly from [*Citius, Altius, Fortius*](https://vimeo.com/100576137) by Felix Deimann and [*Forms*](http://www.quayola.com/forms/) by Memo Atken and Quayola, who used Olympics footage to create elegant and stunning abstract animations. I wanted to make similar, structural abstractions by using motion capture data and automating some of the animation by using scripts in Maya. In addition, I wanted to work with two actors in order to create a collision of forces within the abstraction.

For the content of the animation, we had two actors who knew stage combat and two improv dancers. The first take is a Judo scene; I wanted to emphasize the mirrored movements of the actors by drawing shapes in between them. I went with a triangulated, paper look so that each frame would capture a sort of structure made by both of their bodies. In the end I also incorporated translucency so you can still look for the outline of each actor. The second scene is a sword fight. The curves are the motion paths of the swords, and the spheres hint at the extremeties of each actor's limbs. The two actors are more obvious in this one because I had to use contrasting colors to differentiate the sword paths.

The reason I called this project *Synergy* is because, halfway through my process, I was able to partner up with Irene and Charlotte for some Optitrack/Kinect action. The partnership was essential since we split up all the testing and capturing amongst the three of us. We had a good balance between production, technical, and crafting experience. In addition, working with actors and dancers was stupendous because of their positive attitude and the awareness they had of their own bodies. Without any of these partnerships, I doubt the end product would have come together so harmoniously.

<br>
<img src="https://github.com/michell3/Photos/blob/master/mocap/screen.jpg" width="415" height="295"> <img src="https://github.com/michell3/Photos/blob/master/mocap/sword_2.jpg" width="415" height="295">
<img src="https://github.com/michell3/Photos/blob/master/mocap/kinect.jpg" width="415" height="295"> <img src="https://github.com/michell3/Photos/blob/master/mocap/set.jpg" width="415" height="295">

-

#### WIP

We are still working with the Kinect data that we captured from the dancers, so stay tuned to see what we will do with that! As a sneak peak here are a series of gifs that illustrate our kinect data from three perspectives. We've managed to export that data as CSVs and bring them into Maya as particles. To learn more, check out the [CacheCloud](../michelle/Scripts/CacheCloud) script.

-

#### Process

Our process had several steps involving Optitrack, Kinects, Maya, and etc. Here is a simplified breakdown without the glitches.

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
- Import FBX data
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
  * Rotoscope animation to match timing
- Use 3-point lighting
- Set up camera angles
- Render

*Post Processing in Premiere Pro*
- Sync video, animation, and audio
- Apply phase and pitch shifters to audio

-
#### Links
- [Behind the Scenes](https://vimeo.com/143092931)
- [More Project Images](https://github.com/michell3/Photos/tree/master/mocap)
- [Maya Scripts](../michelle/Scripts)

-
#### Special thanks to
- **Colin-James Whitney** and **Zachary Fifer** (left) for performing the fight scenes for us
- **Javier Spivey** and **Sabrina Clarke** (right) for dancing for us

<img src="https://github.com/michell3/Photos/blob/master/mocap/fighters.jpg" height ="550"> <img src="https://github.com/michell3/Photos/blob/master/mocap/dancers.jpg" height="550">
