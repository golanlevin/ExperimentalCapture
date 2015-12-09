####Final Project
## All about perspective
###--Perspective transformation & 3D Reconstruction from light field image

####Liz Zhang

###The idea
The world in photos is what the photographer sees, in other word, what the photographer notices. We are so used to look at the world from the photographer's perspective that we sometimes forget to ask "what would we have seen if we were there?" So how can we see things differently from a photo already taken? The lytro camera offers one option by letting the user take the photo first and focus on arbitraty object later. But that only makes the object clearer, it remains "stuck" in its "rightful" place and there is nothing it can do about it.

Except with projective transformation we can do something about it. And with a Lytro camera, there are more than one ways of viewing things differently. By constructing homographies and morphing we can theratically bring any object to the real center of the camera as if we are facing right at it. I would like to combine the lytro camera and perspective transformation, so that we not only change the focus of a scene, but also its perspective so the object in question not only becomes clearer, but brought to the center of the stage. Also, since the Lytro camera captures the depth of scene, we can use it to map the pixels to its depth and do 3D reconstruction from a single image. These are the two main ideas I will explore in this project.

###Tools
The tools used for this project are a Lytro Camera, Matlab, Lytro Desktop, and Meshlab

###Process & Result
#### 1. Perspective Transformation
We view the world from different perspectives, the transformation between the object we see from where we stand and another point of view is perspective transformation. This can be easily calculated using homography matrix. Given 4 points (x,y corrdinates) of one image, and 4 matching points of the perspective we want to view the object from, we can reconstruct the image and obtain another perspective of the given object.
Below shows one example:
This is a picture taken from the Carnegie Museum of Art:
![img_0148](https://cloud.githubusercontent.com/assets/11666005/11649129/9d407cc8-9d49-11e5-80ff-bd4cbc99eed0.jpg)
Imagine ourselves floating in the air and view the artwork from mid air, what we see would look like this:
![demo_h_crp](https://cloud.githubusercontent.com/assets/11666005/11649128/9d3d675e-9d49-11e5-837d-d061e56b370a.jpg)

We can do much more if we have the focus length data, which we can easily obtain from the RAW data from Lytro.
With the focus length data we can estimate the depth of objects in a static image. And using methods describted by 
in their paper, we can do 3D reconstruction from a single image for box-like scenes:

Below is a photo I took in the Art Museum:
![img_0144](https://cloud.githubusercontent.com/assets/11666005/11650873/8e90848c-9d5a-11e5-81fa-1b542f5431ec.jpg)

And with perspective transformation, 3D mapping and texturing, I am able to get a box that mimics the original scene:
[![](https://cloud.githubusercontent.com/assets/11666005/11650768/e7fa6322-9d59-11e5-8af6-93efd09e0de5.jpg)](https://vimeo.com/148391778)
![art11-1](https://cloud.githubusercontent.com/assets/11666005/11650939/1f6a738c-9d5b-11e5-9165-be4f107cff1c.jpg)
![art11-2](https://cloud.githubusercontent.com/assets/11666005/11650770/e7fd1fe0-9d59-11e5-820d-05f587b66f58.jpg)


Using similar method, we can refocus on certain object and changing the perspective at the same time.
Below are two scenes I took from the Art Museum. They are found in the sculpture hall, miniatures of the first Thanksgiving in America.

#####A normal photo taken from the front is shown below:

![img_man_front](https://cloud.githubusercontent.com/assets/11666005/11650249/75bbf39c-9d55-11e5-92f2-2b763fb65668.jpg)
The Lytro refocused photos and their corresponding perspective transformed photos:

1)  Focusing on the man in front:
![img_2_man_h](https://cloud.githubusercontent.com/assets/11666005/11650280/a8ccf89e-9d55-11e5-9d2f-48f247d052a2.jpg)
2) Focusing on the group of women sitting in under the arch:
![flock_h](https://cloud.githubusercontent.com/assets/11666005/11650279/a679a222-9d55-11e5-8eb7-7aa35f0fd021.JPG)
3)Focusing on the man holding a plate standing behind:
![img_plate_h](https://cloud.githubusercontent.com/assets/11666005/11650255/7c0e4420-9d55-11e5-86e7-7c9abad8e796.jpg)

#####Another Scene:
![img_back](https://cloud.githubusercontent.com/assets/11666005/11650364/7be3b6b4-9d56-11e5-8b4d-ea1b6e7424df.jpg)
1) Focusing on the child:
![img_child_h](https://cloud.githubusercontent.com/assets/11666005/11650367/860fc3d0-9d56-11e5-8d34-8c58e1adcf47.jpg)
2) Focusing on the cow:
![img_cow_h](https://cloud.githubusercontent.com/assets/11666005/11650368/8611ae5c-9d56-11e5-8042-23e15c96b8d0.jpg)


#### 2. 3D reconstruction using light field data

Using the Lytro Desktop we can extract a depth map and a refocused image. These are the data I used for 3D reconstruction.
Results are shown below:
[![](https://cloud.githubusercontent.com/assets/11666005/11649227/ca3b8a8c-9d4a-11e5-9efb-5058d81cb983.png)](https://vimeo.com/148189063)




