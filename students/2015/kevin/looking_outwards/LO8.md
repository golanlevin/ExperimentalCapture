# Looking Outwards 8: Gaze-Driven Video Re-Editing

This Looking Outward reflects on the paper [Gaze-Driven Video Re-Editing](LO8.pdf).

The research team proposes a method for providing screen size and aspect ratio aware edits of movies by using eye tracking data from viewers.  This method of editing attempts to buypass bottom up systems of re-editing based on CV identification which can't account for the narrative surrounding the frame, by focusing on the user experience of the movie.


One of the issues with the method that was raised in the paper is that because only the focal point is tracked by user eyes, secondary characters can sometimes be cut in half in the edit, when the frame could be shifted slightly to include them in the shot as well.  I wonder why, given the prevelance of libraries for identifying faces and bodies, why there was no content aware smoothing applied to the refocused frame, allowing the frame to shift slightly to accomodate secondary objects that the user may not have focused on.

I'm really surprised that this paper was published so recently, since I feel like I heard this method proposed years ago, but looking through the bibliography it doesn't appear that there has been a great deal of related research in this specific area, which I found surprising.