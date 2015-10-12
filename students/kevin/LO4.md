# Looking Outwards 4: Real-time Non-rigid Reconstruction using an RGB-D Camera

This Looking Outward reflects on the paper [Real-time Non-rigid Reconstruction using an RGB-D Camera](LO4.pdf).

The research team developed a new way to represent 3D objects captured using a depth camera in real time with relatively high levels of detail.  This new approach, which used interpolations and smoothing algorithms from an initial rigid scan, performed at the same level as many off-line algorithms that have more time to reconstruct the model while maintaining 30fps.

While the project examined a number of complex shapes, and acknowledges that the approach doesn't allow for movement which is extremely fast, I would have liked to know how the algorthim performed with a moving camera or subject, rather than maintaining a stationary camera and limited movement to the object.  Would it be possible to film a reasonably paced walk-and-talk in this way?  Or a sweep down and around the head?

The sources were interesting in this paper, because in some cases the researchers proposed additional algorithms or methods that they didn't have time to implement but which they theorize might improve the process even further.  Setting up these further areas of research throughout the paper rather than in a single section at the end provided a lot of interesting questions to think about during the reading.