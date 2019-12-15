//  ld_animToCurve.mel
// 
//  Authors:     Lee Dunham
//  Licence:     Creative Commons, Attribution, Share Alike
//  About:       Create a curve from selected animated objects or vertices.
//  
//  Requires:
//      getfacecenters.py - (Exempt from ld_animToCurve.mel licence)
//      ld_getFaceCenter.mel
//      ld_floatToStringArray.mel
//      ld_animToCurveCmd.mel
//  Usage:
//      ld_animToCurve ;
//      Select animated objects or vertices and execute the command.
//      A curve will be created for each object and/or vert using the timeline.



Place both scripts ("getfacecenters.py" and "ld_animToCurve.mel") into one of mayas script directories
(ie "documents/maya/2011 x64/scripts/") and start Maya.

To Use:
MEL command -

ld_animToCurve ;