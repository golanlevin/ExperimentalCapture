#Using Leap Motion within Unity 3D

![leap](https://cloud.githubusercontent.com/assets/11639631/11856384/37eb1abe-a41e-11e5-87fc-3ca6e18b50c2.jpeg)

## What is it?
Leap motion is a crowd funded project that allows users to be able to see their hands in a virtual space (ei your leap motion can track your hands and relate this info to your computer)

## What Do I use it For?
The leap can be used for any creative project in which controlling something with your hands and fingers can be applied. Most notably, it  can be used in VR experiences to let users have a sense of space by allowing them to see their hands in the world. This is where unity3d combined with the Leap and oculus may come in handy. 

##Caveats: 
The Leap Motion controller uses IR vision in order to see where and is something is a hand. Because of this, occlusions of the hand will give crazy results (forget making a fist) The leap cannot be counted on for precise control! There are also no notable built in gesture recognitions for the leap. You can get around this by adding colliders to your hands in Unity and then focusing on dealing with where the colliders are not where the hand is. There are also a variety of downloadable plug ins for unity which handle leap gesture recognition. Also, because of the IR sensors in the Leap there are a few things leap will not work well with. Fluorescent lights will cause confusion so if you are using leap underneath bright white lights, try moving. Also for some reason the color Black will have major effects on the leap because under fluorescent light, black looks drastically different. This means if you have long black hair and tie it up in a bun, the leap may recognize the bun as a hand, thus causing a ‘ghosting’ hand affect. 

## This tutorial will go through the steps of connecting your leap with your unity 3d game

First, Download your SDK Here:
https://developer.leapmotion.com/downloads

Follow secondary instructions here, it should be good to once you see your hands in the visualizer. Make sure your leap icon on the top toolbar is active

![Title Picture](https://cloud.githubusercontent.com/assets/11639631/11856354/04bb7012-a41e-11e5-80e7-ccef1bf7e9c3.png)<br /> 

Make sure you understand what is happening in the visualizer. There are 2 IR cameras inside the leap that are programmed to look for hands. Since it basically runs on image recognition, the first thing to understand is that the leap is not accurate!  

![Title Picture](https://cloud.githubusercontent.com/assets/11639631/11856395/4fb9850e-a41e-11e5-8ada-19af7dfb5488.png)<br /> 

Second Download the Unity SDK Here:
https://developer.leapmotion.com/downloads/unity

Download The relevant package. You need to make an account with them, but that is fine; they don’t send much spam.

Make sure you have the latest version of Unity! Anything version 5+ should be good. I won’t go through how to work with unity but it should be quick to pick up if you just google the terms I use and research on your own. It is probably the easiest way to work with leap right now. 

Have your new unity3d scene opened and waiting.

After opening the package, you will automatically be taken to your unity scene and an extra window will appear:

![](https://cloud.githubusercontent.com/assets/11639631/11856418/8bdb3a82-a41e-11e5-8921-a629387b241e.png)<br />

Select Import


Now you should have some folders in your assets
Select the Folder Leapmotion -> scene -> LotsOfBlocks

Your main script is Hand controller that is on the GameObject “HandControllerSandBox”, Check it out! Take a look at it’s inspector.

![](https://cloud.githubusercontent.com/assets/11639631/11856445/bb204e68-a41e-11e5-8636-705af08f07a5.png)<br />

The Graphic models lets you choose which hand model to use with the leap; I would suggest using their default hand or if you really want a custom hand, to customize one of the hands that they give you. 
IsHeadMounted: check this box if you are using an oculus with an attached Leap Motion, like so: 

![](https://cloud.githubusercontent.com/assets/11639631/11856471/efca4f88-a41e-11e5-9179-d94e4937ab39.png)<br />

Destroy Hands: This will destroy the hands objects whenever you do not have the hands within the scene (your hands are not currently in front of you)

#Creating a New Scene From Scratch
Assets->LeapMotion->prefabs->HandController
Drag in the prefab to your scene. Now you should see an icon of the leap motion in your scene, move this icon next to the camera to where the leap motion would sit in front of your desk. 
![](https://cloud.githubusercontent.com/assets/11639631/11856491/1be7de6e-a41f-11e5-98e5-f693e234364d.png)<br />
![](https://cloud.githubusercontent.com/assets/11639631/11856494/26bf8ddc-a41f-11e5-88be-9e4049afa109.png)<br />

Test your Placement of the controllers by playing the scene and adjusting from there. Notice how in my pic there is a small box around leap? That is where the hands will manifest. Currently it is way too small, so we can also make that bigger by changing the Scale in the Inspector.
![](https://cloud.githubusercontent.com/assets/11639631/11856512/5082a7c6-a41f-11e5-8c75-af5b81952df7.png)<br />

Better.

After adjusting the placement of your hand controller, Add in some lights (like directionals) in order to brighten your scene. Something to keep in mind when lighting is that shadows help a lot in letting users know where their hand is placed in the scene.
![](https://cloud.githubusercontent.com/assets/11639631/11856534/7c401bd2-a41f-11e5-8604-1d0f2fdaa423.png)<br />

Add in some cubes in your scene. DO NO FORGET TO ADD RIGIDBODIES ON THEM!
Notice that the leap hands have built in rigidbodies and colliders on them as well. 

![](https://cloud.githubusercontent.com/assets/11639631/11856539/86e449aa-a41f-11e5-81f1-c765fc836477.png)<br />

Now, you’ll notice it is hard to actually interact with the world. This is what I mentioned before about gesture recognition, You will have to write some code to let unity know when somebody is trying to pinch/pick up something and so on. To do this I would suggest having code that finds the hand (in my case the minimal robot hand) when it appears and affecting it that way. Otherwise, I would go straight to the hand controller prefab in you scene, double click on ‘left hand graphics model’ and insert your code directly onto the hand model (this will only work if you have only one person using the leap in the scene instead of multiple). Anyway, good luck in constructing gesture recognition for leap! Remember, there is a lot of open source code out there for this stuff, so check those out if you're having trouble. 

Once again, good luck!
