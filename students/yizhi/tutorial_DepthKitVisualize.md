#Depthkit Visualization Tutorial

This tutorial is complemetary to James George's DepthKit toolbox, focusing on how to fully utilize the functions provided in DepthkitVisualize and really make it do what we want.

The installation, caliberation and basic maliputation in DepthkitVisualize is well documented in his own github, I provide the link below for your reference.
https://github.com/obviousjim/DepthKit

Below steps assumes that you already have a depth video and matching color video captured and stored in proper places using Kinect or Xtion.

## The visualizaton tool

In the DepthkitVisualize UI we have a list of all the things that we can tweack with. As shown in the left-hand side in below screenshot:

<img width="972" alt="screen shot 2015-12-11 at 2 43 27 pm" src="https://cloud.githubusercontent.com/assets/11666005/11753845/9a6a540a-a015-11e5-8fed-dddaf9ab3b17.png">

Just as in any video editing tool, these options allows us to add various effects usign keyframes and their value. We can customize these settings and get some crazy warping effect like shown below, we can achieve that by changing its configuration file.
![](https://cloud.githubusercontent.com/assets/11666005/10568180/803b391c-75e2-11e5-9776-59c50fcc44d2.png)

In the above example I mainly changed the XSinAmpt settings in the warp option. It turns out that for every option there is a cooresponding configuration file in .xml, which is how the software is recording the changes we made. So one way to customize these settings is to reverse the process so that instead of letting the software record what we do, we provide it with a configuration file from which the software takes its values.

The configuration files can be found in the composition folder:

<img width="619" alt="screen shot 2015-12-11 at 2 38 51 pm" src="https://cloud.githubusercontent.com/assets/11666005/11753757/15b388bc-a015-11e5-8fa1-d1631c1d64d1.png">

Inside is all the settings in .xml

<img width="602" alt="screen shot 2015-12-11 at 3 03 41 pm" src="https://cloud.githubusercontent.com/assets/11666005/11754310/6b58926e-a018-11e5-8717-1fd8cb6f46d7.png">

In the above example I substituded the XSinAmpt.xml with my own.
![](https://cloud.githubusercontent.com/assets/11666005/10568200/b9aaf336-75e2-11e5-844f-55e01ec3f6e1.png)
This file was then used to generate the wrap motion using DepthKit visualization.

The above signals will then reflect in the waveline shown in the warping when reopening DepthkitVisualize. One can easily make their own configuration in this way. I used a java parser to do that, the code can be found here(https://github.com/elizazhi/Experimental-Capture/tree/master/xmlMaker).



