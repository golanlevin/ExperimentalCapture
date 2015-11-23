#Final Project Proposal: Audio Empathy
##By Kevin M. Karol

For my final project I hope to create an Android and OSX application suite which syncronizes audio playback between the two devices.  To achieve this synchrinozation I will use an audio synchronization protocol I've previously developed, and build on top of it location awarness using the estimote beacon's indoor location SDK.  This location awarness will then factor in the time delay it takes sound to travel from the speaker to the user's ear for better synchronization.  The final product will consist of a javascript render of the relative position of all phones connected, and the ability to "switch" your phone's position so that you can hear how other individuals within an environment experience sound differently from you.

![](Room\ slice.png)
Figure 1: The Javascript output tracking the location of each phone in the room

![](app\ slice.png)
Figure 2: The Mobile application interface for hearing the difference between where you and another observer are.