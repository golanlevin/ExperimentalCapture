#Getting started: The EyeTribe Eyetracker
Written by Will Miao, October 2015

Out of the box and without any additional software, the eyetracker developer kit can record gaze positions for both the left eye and right eye, as well as pupil size, and dump this data into a text file. It can also be used to control the movement of your on-screen cursor, but lacks the ability to click or select anything.

## Set-up
Plug the EyeTribe eyetracker into your computer via USB (note: the eyetracker requires USB 3.0), and place it mounted on the tripod underneath your monitor. Alternatively, if you are using a laptop, the eyetracker fits nicely in the crevice between your keyboard and screen. Avoid moving the eyetracker after it has been calibrated; if the position shifts, you will need to re-calibrate the device in its new position.
![eyetracker placement](https://lh4.googleusercontent.com/mve8PZnq-3EFjpIJMviUW0OSB1akqaC1oamOGHgF7ipgvhoi3g7xCQZfZ7KZlQEyOKeiNp6a9HfKhRCeoRVsgY1FpQtKUkby5mXUif1EcPVIksJH969ERK9vIA)


To use the eyetracker, you must be running the EyeTribe SDK, which can be downloaded from the EyeTribe website (https://theeyetribe.com/order/my-account/). You must be logged-in from an account that has purchased the EyeTribe in order to see download links for the SDK; Golan can provide you with this information.
![SDK download](http://i.imgur.com/5jrDUeP.png)


Once you have the SDK installed, start the application. A dialog box will appear asking if you would like to start the Eye Tribe server -- click Yes. 
![start server dialog](http://i.imgur.com/Hil49do.png)


After starting the server, a terminal window will appear. This window is useful for diagnosing connection issues with the eyetracker; a successful connection is shown below. It took several tries to get a successful connection; if you get messages saying that the eyetracker is not connected, try doing the same.
![server terminal](http://i.imgur.com/yiB7DbN.png)


## Calibration
Once you have the server started successfully, you will be prompted to calibrate the device. You should recalibrate the device anytime its position may have changed.

Click "calibrate" and the calibration exercise will begin. You will be shown a series of points on your screen, and you must move your gaze to each point in succession.
![follow the dot](http://i.imgur.com/TPcVcJx.png)


When the exercise is over, the app will tell you the quality of your calibration. You can move your gaze around the screen to control the red dot. If it doesn't quite follow your gaze, you should recalibrate until it does.
![calibration results](https://lh3.googleusercontent.com/6bjm2x_G2EpexYNfPaIARy2xHKvuCo4X2ULpvYAybuDRTo17l2xwJLHI45bjNFSJQBXzj4Rwb-9x9Uk7V2Y5IJWNop-1pRJ8hFOYoKmRajvKUai3zBcvwRQL9pqWLA)


Once you have a good calibration, the UI will be updated to reflect that.
![good calibration](http://i.imgur.com/mhx2jOe.png)


## Recording gaze data
From the SDK, you can record your gaze. Under the Options tab, click "Launch" to launch to API console.
![launch api console](http://i.imgur.com/RbJVKFn.png)


This will lauch a live feed of your gaze data. However, data will not start recording until you click "Record to file". You will be prompted to define a file location and file name. Once you've done that, hit "OK", and gaze data will begin recording. Click "Stop recording" when you are done.
![record to file](http://i.imgur.com/Zc6n5P8.png)


The drawback to this method is that the output of is quite messy and might be inconvenient for processing. 
![api output](http://i.imgur.com/040ndPJ.png)


An alternative to this approach is using [this program](https://github.com/willzmiao/projects/tree/master/EyeTribe%20Gaze%20Recorder) that fellow ExCap student Ben Snell and I wrote for openFrameworks. This program will output only the timestamp and X-Y gaze coordinates in a CSV file. To begin recording, press "e"; to stop recording, press "e" again. A new csv data file will be generated in your /data folder. The first column is time (in seconds), the second column is the X-coordinate of gaze, and the third column is the Y-coordinate of gaze.
![csv output](http://i.imgur.com/t8vaOLT.png)


## Resources
[EyeTribe Getting Started guide](http://dev.theeyetribe.com/start/)


There are also libraries for ofx and Processing:
openFrameworks: https://github.com/TatsuyaOGth/ofxEyeTribe
Processing: https://forum.processing.org/two/discussion/9901/the-eyetribe-processing-library


It is also worth mentioning that EyeTribe also released beta-version software called EyeProof which automatically generates heatmaps and gaze paths. This is available for Windows only, and can be downloaded from the EyeTribe site (with login).
![EyeProof analytics software](http://i.imgur.com/6EZTRMW.png)




