#Final Project Presentation: Location Synchronized Audio
##By Kevin M. Karol

Baseline Technology:

I developed applications for iPhones/Android Phones to stream audio which syncronize audio with iPads playing back video on stage, a master background audio system, and click tracks for the performers on stage.  The key element to this system is how it allows the audience control over mixing the pre-recorded audio and live performance on their own terms.

![](Poster.jpg)

For this project I used this technology as a jumping off point, with the intention of adding local position awarness in order to account for the physical delay of sound as it travels through space.  Audience members at the back of the theater have the sound of the live performers reach their ear 0.1 seconds later than the front of the theater, which can be enough to noticably pre-empt the beat.  This location awarness would allow for true syncronization of live performers, and pre-recorded media regardless of where you sat in the theater.

###Indoor Location Tracking

To this end I started working with Estimote's iBeacon technology, and indoor postion tracking SDK.

![](estimotePositioning.gif)

This sdk allows each user's phone to triangulate its own position in a pre-set room based on the strength of the BLE signal from the beacons.  However, since the delay is so small, in any context which is not incredibly rhythmic, the delay is negligable, and as a result, I turned my attention to larger space scales.


###GPS Location Tracking

To work at a slightly larger scale, I have begun to adapt the technology to use GPS coodinates instead of indoor location tracking.  An added advantage to this approach is that it requires no additional hardware or setup.


###Possible Applications:

While one of the most compelling features of the technology is the ability to mix live and pre-recorded sound through a pair of headphones

Group Muse Concerts:
https://www.groupmuse.com
