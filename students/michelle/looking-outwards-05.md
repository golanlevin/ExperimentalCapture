
## Looking Outwards 05

### Live Texturing of Augmented Reality Characters from Colored Drawings
#### Disney Research Zurich and the Computer Vision Lab, EPFL, Switzerland
--
#### Project Video
[![Project Video](http://www.iamag.co/features/itsart/wp-content/uploads/2015/10/Live-Texturing-of-Augmented-Reality-Characters-from-Colored-Drawings-5.jpg)](https://www.youtube.com/watch?t=1&v=SWzurBQ81CM)
--
This project tries to use augmented reality as a way of bring back life into traditionally interactive practices. In this case, they are revamping coloring books. The true success of this project is the high quality of its presentation, which had to have a lot of artist involvement since the characters and animations are so convincing. The other success is their straightforward method of live texturing.

Their pipeline is broken into several stages.

The first is the Content creation pipeline, where the artist is most heavily involved. He/she produces a uv-mapped 3D object, an island map (the uv map flattened) and a projected drawing. From there, a lookup map must be created, which basically maps the texture according to the 2D drawing. I find it particularly interesting that they likened the process to the energy of a spring system.

After this step is the live pipeline, which has the modular problems of image processing, template detection, deformable surface detection (for warped pages), and texture creation and mesh rendering. The final interactive coloring book is a Unity build for android and iOS. It accesses the camera data and then sends it to a C++ library to perform the deformabe surface tracking algorithm and generate the 3D shape. The app then projects the data in place and renders the animated 3D character. The texture is filled by retrieving data from the lookup map.

Overall I have to applaud the amount of fun and interaction in this app, and it is something that would definitely profit a company such as Disney since you could only develop the coloring book with top artists and top technicians. Unfortunately I heard that the business unit that purchased this technology may have butchered the execution. I hope the research is able to recover from this or find its way into another form.

--

[Research Paper](http://www.disneyresearch.com/wp-content/uploads/Live-Texturing-of-Augmented-Reality-Characters-from-Colored-Drawings-Paper.pdf)

[Project Website](http://www.disneyresearch.com/publication/live-texturing-of-augmented-reality-characters/)

![Process Images](http://o.aolcdn.com/hss/storage/midas/64313a651371ee92da9e469e742cea5b/202744579/AR-kids-drawings-disney02.jpg)

![More Process Images](http://www.disneyresearch.com/wp-content/uploads/Live-Texturing-of-Augmented-Reality-Characters-from-Colored-Drawings-Image.png)
