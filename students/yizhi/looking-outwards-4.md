#Looking outwards report 4
##Coloring in 3D
####Liz Zhang

http://www.theverge.com/2015/10/5/9453703/disney-research-augmented-reality-coloring-books

This is a product developed by Disney research. The project uses augmented reality to bring coloring books to 3D and make it more realistic for kids.

The details of the technique are discribed in the paper  [Live Texturing of Augmented Reality Characters from Colored Drawings](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=7165658&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D7165658). 

The highlights of this project are:
1. The coloring of the character is automatically synthesized as it is being drawn.
2. A deformable surface tracking algorithm that allows the character to move but stick to the page

The realtime texturing is done by a look-up based algorithm that assigns each pixel in the drawing to a pixel in the 3D model. This method performs better than naive projection and has faster speed than the photoshop content-aware filling algorithm. The deformable surface tracking also performs better than the state-of-the-art technique.

What might be one of its drawback is that although the coloring is real time synchronized, one has to view the process through an iPad to look at the 3D model being colored. Basically one person might find it quite awkward to color the character and look at the 3D model at the same time. What I believe would be a more sensible way is that the coloring can be done on the iPad, so that the person doing the coloring only has to operate behind the screen. But then I guess the whole point of real time synthethising is lost. Fancy technology and practical adoption, it seems hard to keep both.

