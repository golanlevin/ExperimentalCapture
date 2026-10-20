# Full-Body Scan + Reanimation Workshop (2026)

Formerly "Polycam + Mixamo" (2022-2024), this classroom exercise now uses **[Scaniverse](https://apps.apple.com/us/app/scaniverse-3d-scanner/id1541433223)** and **[ActionForge](https://actionforge.app/#clip=idle_loop)**. You'll also need to install **[Meshlab](https://www.meshlab.net/#download)** for model cleanup. 


---

## 1. Capture with Scaniverse

*Our goal is to capture a 3D model of a person in a T-pose. The subject needs to remain very still; consider propping up their hands with tripods.*

Use the free [Scaniverse app](https://apps.apple.com/us/app/scaniverse-3d-scanner/id1541433223) to 3D scan a person in a T-Pose. No purchase or subscription is required. 

When you finish the scan, "Export Model" and create an OBJ file (actually, a ZIP of obj, mtl, and jpg files). Then airdrop the ZIP to your computer for further processing. 


---

## 2. Clean with Meshlab

*Our goal is to remove irrelevant parts of the captured model; to reduce polygon count; and to clean up the model by reducing degeneracies, closing holes, etc.*

Install Meshlab, an open-source 3D editor, from [https://www.meshlab.net/#download](https://www.meshlab.net/#download).

Open your OBJ file into MeshLab. If your files are correctly placed together the same folder, your model should appear textured. 

Use the "Select Faces in a Rectangular Region" button (in the upper right) to select pieces to delete, and delete them with the "Delete Selected Faces and Vertices" button. 

Meshlab can sometimes crash during complicated cleanups. After you're done removing junk faces and vertices, but before you proceed to cleaning and repairing, be sure to save a provisional copy of your model in its own folder, using "Export Mesh As..." `Alias Wavefront Object (*.obj)`.

Now we can remove degeneracies, simplify the model and close some of its holes. In Meshlab: 

* Filter > Cleaning and Repairing > Remove Duplicate Vertices
* Filter > Cleaning and Repairing > Remove Duplicate Faces
* Filter > Cleaning and Repairing > Remove Unreferenced Vertices
* Filter > Cleaning and Repairing > Remove Isolated Pieces (wrt Face Num.) — optional, for eliminating small floating fragments.
* Filter > Remeshing, Simplification & Reconstruction > Simplification: Quadric Edge Collapse Decimation **(with texture)** 
* Filters > Smoothing, Fairing and Deformation > Laplacian Smooth

Make sure to save the final version of your cleaned-up OBJ with a good name, in its own folder.


--- 

## 3. Convert Cleaned OBJ to GLB with Visiomake

*Our goal is to convert the cleaned OBJ model to GLB format. We'll use Visiomake, a free browser-based converter tool that does all computation locally.*

Make sure all of your assets (obj, mtl, jpg) are in the same folder, at the same file hierarchy level.

Zip up the folder containing your OBJ assets (obj, mtl, jpg). 

Go to [https://visiomake.com/en/convert/obj-to-glb](https://visiomake.com/en/convert/obj-to-glb)

Upload the ZIP file, then download the resulting GLB file. 


---

## 4. Rig and Animate the Model

*Our goal is to rig the model (i.e. fit a skeleton to it, which allows it to be bent and animated); add an animated movement to it; and export a new GLB model that includes the rig and animation.*

Go to [https://actionforge.app/#clip=idle_loop](https://actionforge.app/#clip=idle_loop). (For more information, there's a YouTube video [here](https://www.youtube.com/watch?v=FBMEtoKUXL8).)

On the left side, click on the `+ UNRIGGED MODEL` button. Upload your cleaned GLB file from step 3 to add the unrigged model. 

Click the green button, `RIG IT HERE - PLACE THE DOTS`. Your model should load into ActionForge. 

Set the model's height and fingers-setting (hand-type, e.g. mitten). 

It's likely that your model is asymmetrical, so in the lower-left, un-check "Mirror left and right".

Now adjust the joint dots: position the dots for the hips, shoulder, elbows, chin, etc. 

Click `RIG` in the lower left to compute the rig.

Scroll down and click `BIND & WEAR` in the lower left. 

Select an animation for your model, such as "idle_talkingphone_loop" or "dance_loop". 

Click `DOWNLOAD` in the lower right and download an animated GLB file. I recommend renaming your downloaded file so as not to confuse it with your unrigged GLB. 


---

## 5. View your Animated Model(s)

*Our goal is to view all of the students' animations in one scene.*

The professor will provide a common Google Drive dropbox for your animated GLB model. Upload your model to the provided location.

Drag all of the models into [**https://golanlevin.github.io/glbworld/](https://golanlevin.github.io/glbworld/**) To view them together. This is a simple app that I one-shotted in Codex.


<!-- codex resume 01a1587d-559f-7a51-8d0e-b535cc3fce29 -->


---

EOF