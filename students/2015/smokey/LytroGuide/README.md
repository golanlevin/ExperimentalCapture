# The Lytro ILLUM

## Introduction 

Light field camera.

Okay, so you have your hands on your fancy new lightfield camera. You power it on, and press the shutter button. Everything is out of focus, but that doesn't matter, right? Wrong! What's more, You have no idea hell does this thing works! Why doesn't it spit out focus perfect jpg's, and why do none of the buttons do what I want them to do? Also, it's beeping at me in a menacing way. 

Wait, before you give up and buy a Leica, take some deep breaths. We can get through this. Use this camera's similarities to traditional cameras, while understanding the key differences so as not to become needlessly frustrating with a device that works *almost* but *not quite* how one might expect it to.

Well, you're going to actually need to learn the camera. While it utilizes as many traditional camera behaviors/interface elements as it can, the differences from lightfield to regular ("light-plane"?) are significant enough that it *will* affect your workflow, and your creative thought process.

## The Technology Involved.

### Ultra brief overview of traditional camera lenses. 

Cameras use lenses to redirect light, focusing rays of light that enter the lens onto a small plane near the lens, in the camera body. You can stick a film negative or an image sensor on this plane, and - if the camera is in focus - an image will appear.

Lenses have widths, which refers to the angle of view. It's measured in millimeters. Zoomier lenses have bigger numbers. An 18mm lens is wide-angle, 50mm is considered natural (looks similar to our eyes), and 70 and up is considered zoom. 

Lenses have apertures, which affect the quantity (think "intensity" of light reaching the lens). The aperture is just a hole, generally used by sophisticated sliding blades. Lenses used to have bits of metal with holes cut in them that you could slide in and out. If the aperture is closed, less light gets through, and if aperture is open, more light gets through).

Aperture is measured in f-stops, which is a ratio you don't need to worry about. Lower numbers, like f/1.2, f/2, or f/3.5 let in a lot of light. Bigger numbers, like f/8, f/16, f/22, or f/BAJILLION let in less light.

The **important** thing about aperture is that it also affects the depth of field. The depth of field is the range (nearest to farthest distance) that objects will appear in focus. Appearing in focus means that the point of light is not out of focus (a circle of some size) larger than a single pixel of resolution. The image looks sharp.

Shallow depth of field images are achieved with open apetures. They are very difficult to make, from an engineering point of view. Canon sells a 50 mm lens with a mimumum aperture of f/1.8 for $100, and a 50mm lens with a minimum aperture of f/1.2 for $1400.

### Lightfield cameras are different!

The lytro shoots at f/2, always. But it can refocus as if it were shooting at f/16.

Instead of capturing a plane of light data, the Lytro Illum captures a light field. This includes the direction that the light at every point (pixel) is travelling. 

This lets one change the focus of the image during post production. They can also moderatley change the perspective of the image, and combine perspectives to create 3 dimensional images [with only one lens!].

A photographer can also adjust the aperture after-the-fact, although it's worth noting that the effects on brightness are not changed later (more than present technology could) - if a pixel is over or under exposed, there's no recovering that data. 

##First things first

Make sure the battery is charged (use the included charger, not some other charger you found in a cardboard box). Make sure you have an SD card with enough free space to go out and get shooting (at least a gig or two). 

When borrowing the camera, don't go deleting other people's photos without permission. Also, delete your own photos when you are done. This would be **after** the images are transferred **and backed up**.

### BACK UP EVERYTHING! 

## The controls.
Taking photos on the camera is a simple enough task. The camera is automatic. Turn the camera on by pushing the power button (you know, the one that *looks* like any power button).

Push the shutter button, the farthest forward button (with no icon), to capture an image. ("Capture a lightfield"? I'm just going to say "image" or "picture". You're smart, you know what I mean). 

Push the AF button on the back of the camera (the one labelled "AF") for the camera to automatically focus on the current focus point. Adjust the current focus point - the white box on the screen - by tapping the screen where you want to focus. If you don't see the little box, just tap the AF button.

The AEL lock button lockes the current exposure setting while the button is held down. This is very useful, as the automatical camera may want to exposure for the outdoors through a window, leaving your indoor subject dark/"underexposed". Point the camera somewhere (the floor or move closer) where the automatic settings capture the correct exposure, then hold down the AEL button. Move back ("recompose") to the shot you want, and press the shutter button.

The infinity button (the "hyperfocal button") on the camera will automatically set the camera to focus on the hyperfocal distance. The hyerfocal distance is the distance nearest the camera where infinity is still in focus. It is the distance with the largest possible depth of field.

The Lytro button (the one with the icon near the shutter button) is a nifty lightfield feature. A half-press will show you the depth of whatever is at the center of the frame. A full press will give you lots of depth information overlayed on the image. More on how this works (and what all the colors mean) later.

The lens ring closer to the front of the lens will control the focus, and the ring closer to the camera body will control the zoom. *(This is true for almost all zoom lenses on any camera ever. There are some ancient rangefinder lenses that are different, but this arrangement is pretty damn standard).*

Note - on autofocus modes, the front ring on the lens isn't going to do anything. Because, well, duh. 

There are two spinny dials (we call them "dials") on the camera. They change depending on the shooting mode. On "P" Program mode - the one you should use if you don't know better - the front one controls the shutter speed/ISO ratio (doesn't affect exposure), while the rear one controls the exposure compensation.

These are all the controls you need to shoot the basics. Don't forget that the camera is a touch screen, and many features (say, settings) can only be accessed through the touch screen. 

Read about the rest of the controls and menu features at [this webpage](http://manuals.lytro.com/illum/capture-mode/).


### Looking at photos (on the camera)

Press the FN button, or swipe left, to go to playback mode.

Here you can adjust the focus by tapping on different areas.

## The Refocusable Range(s)

Blue and orange! Whether bars on the side, or data layed over the image! These are maps of refocusable ranges. 

The camera, thanks to magic* is capable of capturing depth information. The point between the blue and orange zones is the optical focus - the traditional camera focus. Let's call it 0. Lets increase values as we go farther from the camera (1, 2, 3, etc). Lets decrease as we get closer to the camera. (-1, -2. -3).

Don't worry about units. These are just depth values.

-10 depth values to +10 are the equivalent depth of field as given by an f/16. (This is dependent )

-4 and +4 depth values can **always** be super sharp when refocused later. These are the brightest blue (closer than optical focus) and the brightest orange (farther than optical focus) in the image. The camera automatically chooses -4 for most subjects when autofocusing on a point. 

*Actually, advanced engineering.

## What this means when shooting

When taking photos, you want to take advantage of the full depth of field that the Illum offers. You want your subjects - your forground, subject, and background, all to occupy ranges within our blue/orange zone. This means we *can* focus on them later.

What's more, we want the objects to take up as much space as possible in this range. We want our closest subjects to be at the start of the range, and the farthest ones right near the back. This way we can still focus on everything, but we have the most extreme (and most control, later) when it comes to shifting perspective, doing stereoscopic 3D, and adjusting focus. 

You want the range to have a tight fit within the refocusable range in order to utilize our depth in later images.

