# Final Project Proposal

### Idea #1

Many places around the world are inaccessible from Google Street View and still quite hard to visualize in 3D from Google Earth. These areas that might lack roads and infrastructure, consist of informal housing, or are simply less dense (and less important) then major cities. This is how Caracas's biggest slum looks like from Google Earth:

<img src="images/petare-earth.png" width="300px" />

It looks exactly the same from Google Street View because there aren't any real streets that pass through the slum. This is problematic. It's hard to build infrastructure and protect these dwellings from mudslides without a good layout of the land and the topology. Drone mapping would be a cheap and simple way to get a 3D model of a space like this. It is also a technique that has been used in various disaster recovery scenarios - like the recent earthquake in Nepal - to get a cheap, quick map of a space where traditional mapping techniques would take too long. 

For this project, I'd like to attempt to create such a model using a drone and photogrammetry. A particular software called Pix4D aids in the capture of the drone data - it makes sure you're capturing enough overlap - and then gives you an environment to perform photogrammetry. The results look like this (the Christ in Rio):

<img src="images/christ.jpg" width="300px" />

I could then do quite a few things with the 3D model: maybe visualize some data on it or port it into Unity to create a scene. 

##### What I Need

* Pix4D software: I've obtained an educational trial license
* A phantom vision drone: I've tested out a Parrot drone and also a Phantom 1 drone from ArtFab. I'd like to test the Vision out next week. 

##### Thoughts and Questions

* I'll have to pick a place that is accessible to me around Pittsburgh, but I remain undecided about what kind of place or buildling/structure to map. There are some industrial- and abandoned-looking areas around the river that could be easy to map given the space and the lack of people. 

### Bakcup idea #2

Alternatively, I'd like to at least attempt to callibrate the data from 3 kinects that we used to capture dancer and boxer scenes for project #2. They were all positioned at the same height but in different sections of the room. It would be great to visualize an almost 360 degree point cloud from the 3 kinects. Our friends at Specular also said they could share some callibration code so I could perform the excercise again with 4 kinects. 

