
NOTE: This MayaCacheCloud.0.9.0.py script has been modified

---

Instructions for installing script on Mac:

0. Note that the 'particles' folder is no longer a default folder created by Maya.
   It is instead called 'cache/particles', so I recommend going into the project settings
   and changing 'cache/particles' to 'particles'

1. Copy 'MayaCacheCloud.py' script into
   ~/Library/Preferences/Autodesk/maya/2016/scripts/
   Use cmd+shift+G to navigate there

2. In Maya, open the command-line terminal and open a Python tab
   Type the following lines in the terminal:

   import MayaCacheCloud
   reload(MayaCacheCloud)

   Then save the script to shelf

3. You're done! Running the script should now prompt the
   Cache Cloud dialogue

Instructions for formatting csv files:

1. Make sure csv's are exported as Windows csv's
2. Make sure 3-4 columns of data are provided
3. Make sure animation csv's are zero-indexed and padded
4. Clean up data by removing duplicates in Excel

Instructions for using the point cloud data:

Once the data is in Maya, remember to use the Mental Ray plugin to render particles

---

Original Header text:

*** Cache Cloud ***
Version 0.8
by Daniel Vasquez 
Updated: August 12, 2011
Email: dan@heylight.com
Web: heylight.com

Description:
Python script that creates Maya Particle Disk Cache (PDC) files from a sequence of point cloud data, and also gives you the choice of importing a single point cloud. It could be useful with all the open source data being released from Kinect hacks or 3D scanners. You can start by playing around with Radiohead's House Of Cards data: http://code.google.com/p/radiohead/downloads/list

Tags: 
point cloud, maya, PDC, particle disk cache, python, data visualization, kinect, 3D scanner

Notes:
1) The point cloud data source files should be named serially (with numbers in suffix), with padding. Currently it doesn't take numbered prefixes very well. That said, you might have to rename/serialize your source files appropriately - for example, "frame001.txt" or "dynamite01.csv". Here's a good program to do so on a Mac: http://www.pathossoftware.com/Rename/Rename.html
2) For a point cloud animation, you can select a range of ordered files or a single file. If one file is selected, all files in the animation sequence will be cached.
3) This version accepts CSV and TXT files containing arrays* in the form of:

    integer, float, float, float 
    OR
    float, float, float, integer 
    OR
    float, float, float
    
    *per line, comma-separated or whitespace-separated. Try another form of arrays at your own risk.
4) There's a bug that makes Maya crash when you play the animation past the last frame of the cache. The script automatically sets it to the appropriate timeslider range, so in the meantime just avoid changing the timeslider playback range.  
5) For a single point cloud, the extra attribute selected is added automatically; for animated point clouds, you need to manually add the selected attribute after closing Cache Cloud.
6) Be aware that this script creates a new cache folder and a CacheCloud_history.txt file in your Maya workspace (in the particles directory).
7) This script has only been tested in 64-bit Maya 2011 running on OSX, but I don't see why it wouldn't work in Windows. The UI prompts are called from Maya commands.

License: 
The Cache Cloud script is made available under the Creative Commons Attribution-Noncommercial-Share Alike 3.0 License.
This license lets you remix, tweak, and build upon Cache Cloud non-commercially, and although your new works must also acknowledge Daniel Vasquez (heylight.com) and be non-commercial, you donÕt have to license your derivative works on the same terms.
For more information on this license, read http://creativecommons.org/licenses/by-nc/3.0/legalcode and http://creativecommons.org/licenses/by-nc/3.0/

Things to do:
¥ Minimize code redundancy.
¥ GUI for making particle and attributes more customizable. 
¥ Give option for modifying the point cloud data. For example, remove all repeated points, ease translation of position by a factor, or scale up/down.
¥ Currently this script creates a default particle disk cache using mc.dynExport, which might not be necessary. 
¥ Figure out the bug that's making Maya crash (see notes above). 
¥ Allow flexibility with particleId.
