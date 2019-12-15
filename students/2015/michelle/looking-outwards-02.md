## Looking Outwards 02

### LazyFluids: Appearance Transfer for Fluid Animations
#### O. Jamriska, J. Fiser, P. Asente, J. Lu, E. Schechtman, D. Sykora

In this paper, researchers from the Czech Technical University and Adobe Research present a method of transferring a static or video image texture (an exemplar) to a fluid animation. There approach involves two imputs: a fluid element exemplar and a sequence of target alpha masks. From these elements, their process captures the desired appearance, shape, and motion of the target fluid animation so that the result has a coherent fluid movement and respects boundary-specific effects (i.e. dissipating fog or external flickering flames).

What I found most interesting about this paper was the fact that they had an underlying "uniformity constraint" in order to address the issue of appearance degradation from using "patches". They implemented patch uniformity by using a nearest-neighbor field, in which all patches select their best matching candidates. This paper is very heavy in algorithm-talk, but basically their nearest-neighbor approach allows them to add influences in the candidate selection process to also address issues sucj as temporal coherence and joint formulation. Other transitional issues and boundary effects seemed to be solved with a combination of blurring and masks.

In comparison to the other lazy fluid simulations presented, I found their methodology to be quite promising. I'm impressed by the application of the nearest neighbor algorithm, because I image fluid simulation to involve a lot of calculated trajectories. There are still some glaring issues to an artists' eye, but it does provide a quicker alternative than full-on liquid simulation, which is quite cumbersome in graphics.

[Project Paper](http://dcgi.felk.cvut.cz/home/sykorad/Jamriska15-SIG.pdf)

[![Project Video](http://img.youtube.com/vi/6naNA2sle98/0.jpg)](https://youtu.be/6naNA2sle98)
