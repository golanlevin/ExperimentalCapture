## Tutorial: Agisoft PhotoScan Professional Edition

In this tutorial I will go over the basics of generating an OBJ file using [**Agisoft Photoscan Professional Edition**](http://www.agisoft.com/). All of this information and more can be found in the official user manual linked below. Note that this tutorial is for version **1.1.6** and uses **Mac OSX** screenshots but this can also be used on **Windows** or **Debian/Ubuntu**.

--
### Installation

Go to the [installation page](http://www.agisoft.com/downloads/installer/) on the Agisoft website and download the professional edition installer for your operating system.

![Installer](https://github.com/michell3/peppers-pig/blob/master/Project%20Images/agisoft_download.png)

After the download, open the application.

![Icon](https://github.com/michell3/peppers-pig/blob/master/Project%20Images/agisoft_download.png)

Enter your license code or continue in demo mode to activate your software. If you use demo mode, be aware that you cannot save the project, export reconstruction results, or use some Python commands. After activation, you can move on to using the program.

--
### The Agisoft Workflow

Upon opening the software, you are faced with a new project window.

![New Project](https://github.com/michell3/peppers-pig/blob/master/Project%20Images/new_window.png)

The left panel is the **workspace** where you can manage your **cameras**. Cameras are basically the camera perspective contructed from each photo you upload. In the workspace you can add and remove cameras, manage chunks, and etc.

The bottom panel is for photos, so you can preview and manage your thumbnails.

The 3D view is where you can see your cameras, point clouds, and/or mesh once you've constructed them. To navigate the 3D view, you can **click + drag** to rotate, **ctrl + click + drag** to pan, and **shift + click + drag** to zoom.

Lastly the toolbar has icon shortcuts for most of the functions that you'll be using. In this tutorial I will just be accessing those functions through the **menu bar**. And within the menu bar, most of the functions you need for reconstructing a pointcloud or mesh are found in the workflow menu. In order to export an OBJ, we will basically be hopping down the menu in order to perform the following steps:

1. Add photos
2. Align photos
3. Build Mesh
4. Build Texture

Throughout these stages, you can use the functions under **View**, **Tools**, and **Photo** to do corrective changes and etc.

--
### Tutorials
* [Agisoft PhotoScan User Manual (English)](http://www.agisoft.com/pdf/photoscan-pro_1_1_en.pdf)
