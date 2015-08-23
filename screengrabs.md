#Preparing Screenshot Documentation 

For some assignments you will be asked to document your work with screengrabbed images and/or videos. Such media are likely to remain viewable for many more years than your software remains functionally executable. This page lists three techniques, for preparing:
<ul>
	<li><em>Screenshot images</em></li>
	<li><em>Screengrabbed videos</em></li>
	<li><em>Animated GIFs</em></li>
</ul>

<hr />

<h2><strong>Making and Saving Screenshots
</strong></h2>
You can take a screenshot of your software with an external tool, or sometimes from within the app itself. You can then use <a href="http://www.dwphotoshop.com/photoshop/screenshot.php">Photoshop</a>, <a href="http://omitsoft.blogspot.com/2008/03/taking-screenshots-with-gimp.html">Gimp</a>, <a href="https://pixlr.com/editor/" target="_blank">Pixlr</a> (in a browser) or any number of utilities to crop and adjust the image.  All operating systems have a native screenshot function. Go here to learn how:
<p style="padding-left: 30px;"><strong><a href="http://www.take-a-screenshot.org/" target="_blank">http://www.take-a-screenshot.org/</a></strong></p>


Another method is to save a frame <em>computationally</em>, directly from your software itself. Here is a list of techniques for obtaining or exporting screen images from a variety of popular arts-engineering toolkits:
<ul>
	<li><a href="http://p5js.org/" target="_blank">p5.js</a>: <a href="http://p5js.org/reference/#/p5/saveCanvas" target="_blank">saveCanvas</a>() or <a href="http://p5js.org/reference/#/p5/saveFrames" target="_blank">saveFrames</a>()</li>
	<li><a href="http://processing.org/reference/saveFrame_.html">Processing</a>: <a href="http://processing.org/reference/saveFrame_.html" target="_blank">saveFrame</a>()</li>
	<li><a href="http://www.openframeworks.cc/documentation?adv=yes&amp;detail=ofUtils#ofSaveScreen">OpenFrameworks</a>: <a href="http://www.openframeworks.cc/documentation/utils/ofUtils.html#ofSaveScreen" target="_blank">ofSaveScreen</a>(string filename) &amp; <a href="http://www.openframeworks.cc/documentation/utils/ofUtils.html#ofSaveFrame" target="_blank">ofSaveFrame</a>()</li>
	<li>Cinder: use <a href="http://libcinder.org/docs/v0.8.2/classcinder_1_1app_1_1_renderer.html">app::Renderer::copyWindowSurface(Area &amp;area)</a> to copy the screen into a file, then save it manually</li>
	<li><a href="http://wiki.puredata.info/en/pix_snap2tex">PureData GEM</a>: [pix_snap2tex]</li>
</ul>

<hr />

<h2><strong>Making Screen-Grabbed Video</strong></h2>

To record video of your app running, you will need a screen recording application:
<ul>
	<li><a href="http://www.youtube.com/watch?v=M6Me2V8oUbc">QuickTime X</a>: Mac (<strong><a href="http://www.askdavetaylor.com/record_mac_screen_capture_recording_movie_quicktime_player.html" target="_blank">tutorial here</a></strong>)</li>
	<li><a href="http://www.techsmith.com/camtasia.asp">Camtasia</a>: Win, Mac</li>
	<li><a href="http://www.telestream.net/screen-flow/overview.htm">ScreenFlow</a>: Mac</li>
	<li><a href="http://www.ambrosiasw.com/utilities/snapzprox/" target="_blank">SnapZ Pro X</a>: Mac</li>
	<li><a href="http://www.araelium.com/screenflick/" target="_blank">ScreenFlick</a>: Mac</li>
</ul>
After you have recorded your video, it might be nice to do some editing. Consider using Premiere, AfterEffects, FinalCut, iMovie, Windows Movie Maker, etc. A voiceover and/or subtitles can be especially helpful.

Once you have made a screen-grabbed video, consider adding a narration soundtrack in which you are explaining what's going on. You will then need to upload your video to a host such as YouTube or Vimeo.

<hr />

<h2><strong>Making Animated GIFs </strong></h2>
Animated GIFs are robust, simple, and durable ways to document moving imagery. The easiest way to make one, is to screengrab directly to an animated GIF with <strong>LICEcap</strong>:
<p style="padding-left: 30px;"><strong><a href="http://www.cockos.com/licecap/" target="_blank">http://www.cockos.com/licecap/</a></strong></p>
Another alternative is to save out a sequence of frames, such as with the <a href="http://p5js.org/" target="_blank">p5.js</a> <a href="http://p5js.org/reference/#/p5/saveFrames" target="_blank">saveFrames</a>() function, and compile these into an animated GIF. Here are some other techniques for doing so:
<ul>
	<li><a href="http://gifmaker.me/" target="_blank">Animated GIF maker</a> (online/in-browser tool)</li>
	<li><a href="http://www.digitaltrends.com/social-media/how-to-make-an-animated-gif/" target="_blank">Animated GIFs using Photoshop</a> (tutorial)</li>
</ul>