## condensed version of owen burgess (2009) getfacecenters.py script 
# script that returns the center point of selected polygon faces. 
# owen burgess 2009
import maya.OpenMaya as om
import math

def faceCenter():
    selection = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(selection)
    iter = om.MItSelectionList(selection,om.MFn.kMeshPolygonComponent)
    
    while not iter.isDone():
        dagPath = om.MDagPath()
        component = om.MObject()
        iter.getDagPath(dagPath,component)
        polyIter = om.MItMeshPolygon(dagPath,component)
        while not polyIter.isDone():
            i = 0
            i = polyIter.index()
            center = om.MPoint
            center = polyIter.center(om.MSpace.kWorld)
            point = [0.0,0.0,0.0]
            point[0] = center.x
            point[1] = center.y
            point[2] = center.z
            polyIter.next()
        iter.next()
    
    return point