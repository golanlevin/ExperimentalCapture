
## Looking Outwards 08

### Computer-Generated Watercolor
#### Cassidy Curtis, Sean Anderson, Joshua Seims, Kurt Fleischery, David Salesin
#### University of Washington, Stanford University, Pixar Animation Studios

![Pears](http://otherthings.com/uw/watercolor/images/StillLife.jpg)
![Strokes](http://blog.kim-ash.com/wp-content/uploads/2012/11/compWC.png)
--

This paper explores how to achieve different watercolor effects using several layers of fluid simulation applied to generated paper textures. These simulated effects include dry-brush, edge darkening, backruns, granulation and separation of pigments, and flow patterns. The fluid simulation is implemented in a 3-layer model that reflects the physical processes of how watercolor is applied and absorbed into the watercolor paper. The watercolor paper is a height field psuedo-randomly generated to match the various fibrous textures of watercolor paper. The parameterization of each process includes a wet area mask, velocity and pressure of the water, concentration of pigment in the water, slope of the paper's surface, and the viscous properties of the watercolor medium. The main loop code for this is really straightforward:

For each time step:
- Move Water
- Move Pigment
- Transfer Pigment
- Simulate Capillary Flow

But of course the implementation is really complex.

The applications of this research resulted in a paint program that simulates watercolor painting, as well as automatic watercolorization. I find the automatic watercolorization to be an incredibly fascinating result. It's done in two steps: color separation and brushstroke planning. One daunting aspect of the color separation process is that they use brute force methods to determine the set of thicknesses for each pigment. In addition, the brushtroke planning still has a degree of user selection.

--

[Research Paper](http://grail.cs.washington.edu/projects/watercolor/paper_small.pdf)
