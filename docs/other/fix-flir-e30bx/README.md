### Disabling the information overlay on the FLIR E30bx

The FLIR E30bx is a portable thermal camera, primarily intended for prosumers, which internally runs Windows CE. It has a reticule and FLIR logo burned into all images and video, which cannot be disabled from its control panel. These obscure nearly 10% of the camera's usable pixels. 

In a phone conversation with FLIR customer service, they informed me that they made it impossible to disable the information overlay—in order to ensure that all of the YouTube videos uploaded by "ghost hunters" would include the FLIR logo. 

FLIR made a special configuration file that allows you to *temporarily* disable the image overlay. To configure the camera:

1. Download the attached files below and save them to the SD card.
2. Plug the SD card into the camera and select *Settings*, then the *Information* tab.
3. At the bottom of the window select "update firmware" and pick "Overlayer_off".
4. When the camera reboots the overlay should be off on the LCD screen and the composite video output.

Note that the scale may re-appear when saving and recalling JPEGs on the camera, in which case you will need to run the update again to turn off the overlay.

Here are the files:

* [Overlayer_OFF.fif](Overlayer_OFF.fif)
* [Overlayer_ON.fif](Overlayer_ON.fif)
* [eFLIRInstall.exe](eFLIRInstall.exe)