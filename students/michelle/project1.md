## Project 01

### Pepper's Pig
#### Project Members: [Michelle Ma](../michelle/index.md), [Vidya Vinnakota](../vidya/index.md)
-
#### Project Video
-

#### Concept

Our original inspiration for this project came from the Pepper's Ghost illusion that you can easily create with any LCD screen and clear plastic. We were especially influenced by this video on [How to Turn Your iPhone into a 3D Hologram](http://www.telegraph.co.uk/technology/mobile-phones/11780393/How-to-turn-your-phone-into-a-3D-hologram-projector.html). Of course, it's not an actual hologram, but it projects the iPad screen perpendicular to the viewer's line of vision to create an amazing suspended effect. There are a number of companies who have tried to capitalize on this concept such as [Youlalight](http://youlalight.com/en/3dpiramidforipad), however we wanted to take advantage of the affordable nature of its implementation, and also enrich the experience by adding the interactivity of an iPad.

So we decided to give my Piggy Bank a new life using this illusion. The Piggy Bank was the perfect choice because it was a childhood object, it involves a unique interaction, and it has personality. And since we wanted to give it a new life, we decided to play with its 3D mesh and give it new forms.

*Piggy Bank Image*

-

#### Process

Our process has several parts, involving many programs and machines. Here is the break down.

*3D Scanning*
- 3D scan the subject using **123D Catch** for the iPad
- Reduce and clean the geometry using **Maya** and the **DynaMesh** feature in **ZBrush**

*Generating Forms with Maya*
- Generate new renditions of our piggy using **MEL scripting in Maya**
- Format their pivots and export the OBJs for **Unity**

*Interactions in Unity*
- Implement touch interactions with 3D objects, including rotate and spawning
- Adjust the standard shader to give the right appearance
- Use the **Unity Remote** to debug the program in real time

*Build on iOS*
- Deploy the Unity build for an iPad 4 using **XCode7**, which thankfully allows developers to build on devices for free starting this year

*Construct the Pyramid*
- Calculate proportions of pyramid
- Lasercut on clear acrylic (prototype) and black-tinted acrylic
- Assemble with acrylic cement

-
#### Special thanks to
- **Roberto Andaya** for laser cutting and assembling the pyramid
- [**The Studio for Creative Inquiry**](http://studioforcreativeinquiry.org/) for accepting our Microgrant application to purchase an iPad and other supplies

