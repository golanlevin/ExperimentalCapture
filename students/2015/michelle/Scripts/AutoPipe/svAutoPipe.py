# AUTOPIPE & CENTRE UVS

'''
INSTALLATION:-
Place the svAutoPipe.py file in your Maya scripts directory eg..

C:\Users\'YOUR USER NAME'\Documents\maya\2016\scripts

Then start maya...

TO USE AUTOPIPE:
add the below line to your shelf or run in a python tab/command line

import svAutoPipe as svAutoPipe
svAutoPipe.autoPipes()
	
TO USE CENTRE UVS:
add the below line to your shelf or run in a python tab/command line

import svAutoPipe as svAutoPipe
svAutoPipe.CentreUVs()
	
'''


import maya.cmds as cmds
import maya.mel as mm
import math

def CentreUVs():
	objSel = cmds.ls(sl=True)
	
	try:
		for item, x in enumerate(objSel):
			cmds.select('%s.map[*]' %objSel[item])
			mm.eval("PolySelectConvert 4;")
			mm.eval('TranslateToolWithSnapMarkingMenu')
			objPiv = cmds.getAttr('%s.uvPivot' %objSel[0])
			mm.eval('MarkingMenuPopDown')
			objCenterU = 0.5 - objPiv[0][0]
			objCenterV = 0.5 - objPiv[0][1]
			cmds.polyEditUV(u=objCenterU, v=objCenterV, r=1)
			cmds.select(objSel)
	except ValueError:
	
		objQuery = cmds.listRelatives(objSel[0], ap=True)
		cmds.select('%s.map[*]' %objQuery[0])
		mm.eval("PolySelectConvert 4;")
		mm.eval('TranslateToolWithSnapMarkingMenu')
		objPiv = cmds.getAttr('%s.uvPivot' %objQuery[0])
		mm.eval('MarkingMenuPopDown')
		objCenterU = 0.5 - objPiv[0][0]
		objCenterV = 0.5 - objPiv[0][1]
		cmds.polyEditUV(u=objCenterU, v=objCenterV, r=1)
		cmds.select(objQuery)

# AutoPipe

class autoPipe():

	'''
	sx=1		- scale X
	sy=1		- scale Y
	sdv=50		- subdivision V
	sdu=12		- subdivision U
	tap=1		- taper
	degs=3		- degrees curvature (1=linear)
	subCurve=1 	- subCurves for animating length
	clean=0		- minimum history
	do_uvs=1	- automatic uv system
	rbc=1		- rebuild curves (biggest slow down when animating)
	subd = 50 	- curve subdivisions on rebuild
	tol = 0.0001- rebuild curves tolerance - adjust this if you get curve wobbles
	'''	
	
	def __init__(self, sx=1, sy=1, sdv=50, sdu=12, tap=1, degs=3, subCurve = 0, clean = 0, do_uvs=1, rbc=1, subd = 50, tol=0.001):
		self.sx = sx
		self.sy = sy
		self.sdv = sdv
		self.sdu = sdu
		self.tap = tap
		self.degs = degs
		self.subCurve = subCurve
		self.clean = clean
		self.do_uvs = do_uvs
		self.rbc = rbc
		self.cSubd = subd
		self.cTol = tol
		self.ko = 0
		self.rev = 0

	def autoPipeUI(self):
		if cmds.window('aPipe', exists=True):
			cmds.deleteUI('aPipe')
		
		cmds.window('aPipe', t='Auto Pipe v0.3', mnb=0,mxb=0, w=200, bgc=(0.3,0.4,0.5), rtf=True,ret=1, s=1)
		
		aForm = cmds.formLayout(nd=100)
		
		aCb = cmds.columnLayout(bgc=(0.15,0.15,0.15), w=200)
		cmds.setParent(aForm)
		aCa = cmds.columnLayout(rs=2)
		
		aRa = cmds.rowLayout(nc=8, cat=[(1,'both',5),(2,'right',5),(4,'both',5)])
		cmds.text("Scale X:")
		self.sXTxt = cmds.textField( w=35, tx=1, ec=lambda *args: self.sX(), cc=lambda *args: self.sX())
		cmds.text('Scale Y:')
		self.sYTxt = cmds.textField( w=35, tx=1 , ec=lambda *args: self.sY(), cc=lambda *args: self.sY())
		cmds.setParent('..')
		
		aRb = cmds.rowLayout(nc=8,cat=[(1,'both',5),(2,'right',5),(4,'both',5)])
		cmds.text('Subd V:')
		self.sVTxt = cmds.textField( w=35, tx=50 , ec=lambda *args: self.sX(), cc=lambda *args: self.sV())
		cmds.text('Subd U:')
		self.sUTxt = cmds.textField( w=35, tx=12, ec=lambda *args: self.sU(), cc=lambda *args: self.sU())
		cmds.setParent('..')
		
		aRc = cmds.rowLayout(nc=8, cat=[(1,'both',5),(2,'both',6)])
		cmds.text('Taper:')
		self.sTaTxt = cmds.textField( w=35, tx=1, ec=lambda *args: self.sTap(), cc=lambda *args: self.sTap() )
		self.aKee = cmds.checkBox(l='Keep Original   ', cc= lambda *args: self.keepOrig() )

		cmds.setParent('..')

		aRi = cmds.rowLayout(nc=8)
		try:
			self.Exe = cmds.iconTextButton(l='          EXECUTE    ', style = 'iconAndTextHorizontal', i='extrude.png',bgc=(0.2,0.3,0.4), fla=0,w=175, c=lambda *args: self.execute())
		except:
			self.Exe = cmds.iconTextButton(l='          EXECUTE    ', style = 'iconAndTextHorizontal', i='extrude.png',bgc=(0.2,0.3,0.4), w=175, c=lambda *args: self.execute())
		cmds.setParent('..')

				
		cmds.setParent(aCb)
		aFa = cmds.frameLayout(l='ADVANCED OPTIONS', cll=True, cl=True, w=200,bgc=(0,0,0), pcc=lambda *args: self.resize())
		
		cmds.separator(style='in', h=5, w=200)
		
		aRe = cmds.rowLayout(nc=8, cal=(1,'left'), cat=(1,'left',10))
		self.aLin = cmds.checkBox(l='Linear   ', cc= lambda *args: self.curveSmooth() )
		self.aAni = cmds.checkBox(l='Animate   ', cc= lambda *args: self.animate() )
		self.aUvs = cmds.checkBox(l='UVS   ', cc=lambda *args: self.uvs(), v=1)
		cmds.setParent('..')
		
		cmds.separator(style='in', h=5, w=200)
		
		aRg = cmds.rowLayout(nc=8, cal=(1,'left'), cat=(1,'left',10))
		self.cleanCB = cmds.checkBox(l='Clean   ', cc= lambda *args: self.qClean(), ann='If on, pipe with no history or attributes is created' )
		cmds.button(l='Clean Up', c= lambda *args: self.cleanUp(), ann='Use this to remove history and autopipe attributes from an object created by Autopipe' )

		cmds.setParent('..')
		
		cmds.separator(style='in', h=5, w=200)
		
		aRh = cmds.rowLayout(nc=8,cal=(1,'left'), cat=[(1,'left',10),(2,'left',20)])
		
		self.aReb = cmds.checkBox(l='Rebuild Curve', cc=lambda *args: self.rebuildCurves(), v=1)
		self.aRev = cmds.checkBox(l='Reverse', cc=lambda *args: self.cReverse(), v=0)

		cmds.setParent('..')
		
		cmds.separator(style='in', h=5, w=200)		
		
		
		aRf = cmds.rowLayout(nc=8,cal=(1,'left'), cat=[(1,'left',10),(2,'left',10)])
		
		self.aUACCB = cmds.checkBox(l='', v=0)
		self.aUSC = cmds.button(l='Load Selected', c=lambda *args: self.loadCurve(),ann='Click to load an alternative curve to use - click checkbox to enable')

		cmds.setParent('..')
		cmds.separator(style='in', h=5, w=200)		
		
		aRg = cmds.rowLayout(nc=8,cal=(1,'left'), cat=(1,'left',10))
		cmds.text('Subdivisions: ')
		self.aSubTxt = cmds.textField( w=30, tx=50, ec=lambda *args: self.curveSubd(), cc=lambda *args: self.curveSubd() )
		cmds.text('  Tol: ', h=30)
		self.aTolTxt = cmds.textField( w=45, tx=0.0001, ec=lambda *args: self.cTolerance(), cc=lambda *args: self.cTolerance())
		cmds.setParent('..')
		
		cmds.formLayout(aForm, e=True, af=[(aCa, 'left', 10), (aCa,'top',10), (aCb, 'top', 125), (aCb, 'left',0), (aCb, 'bottom',5) ], ac=(aCa, 'bottom', 5, aCb))
		cmds.showWindow()
		cmds.window('aPipe', e=True, h=30)
		
	def qClean(self):
		getClean = cmds.checkBox(self.cleanCB, q=True, v=True)
		if getClean:
			self.clean = 1
		else:
			self.clean = 0
		
	def resize(self):
		cmds.window('aPipe', e=True, h=30)
				
	def sX(self):
		self.sx = float(cmds.textField(self.sXTxt, q=True, tx=True))
		print self.sx
		return self.sx
		
	def sY(self):
		self.sy = float(cmds.textField(self.sYTxt, q=True, tx=True))
		print self.sy
		return self.sy
		
	def sU(self):
		self.sdu = float(cmds.textField(self.sUTxt, q=True, tx=True))
		print self.sdu
		return self.sdu
		
	def sV(self):
		self.sdv = float(cmds.textField(self.sVTxt, q=True, tx=True))
		print self.sdv
		return self.sdv		
		
	def sTap(self):
		self.tap = float(cmds.textField(self.sTaTxt, q=True, tx=True))
		print self.tap
		return self.tap	

	def keepOrig(self):
		if cmds.checkBox(self.aKee, q=True, v=True) == 1:
			self.ko = 1
		else:
			self.ko = 3
		print self.ko
		return self.ko

	def curveSmooth(self):
		if cmds.checkBox(self.aLin, q=True, v=True) == 1:
			self.degs = 1
		else:
			self.degs = 3
		print self.degs
		return self.degs

	def animate(self):
		if cmds.checkBox(self.aAni, q=True, v=True) == 1:
			self.subCurve = 1
		else:
			self.subCurve = 0
		print self.subCurve
		return self.subCurve
		
	def uvs(self):
		if cmds.checkBox(self.aUvs, q=True, v=True) == 1:
			self.do_uvs = 1
		else:
			self.do_uvs = 0
		print self.do_uvs
		return self.do_uvs
		
	def cReverse(self):
		if cmds.checkBox(self.aRev, q=True, v=True) == 1:
			self.rev = 1
		else:
			self.rev = 0
		print self.rev
		return self.rev

	def rebuildCurves(self):
		if cmds.checkBox(self.aReb, q=True, v=True) == 1:
			self.rbc = 1
		else:
			self.rbc = 0
		print self.rbc
		return self.rbc
		
	def curveSubd(self):
		self.cSubd = float(cmds.textField(self.aSubTxt, q=True, tx=True))
		print self.cSubd
		return self.cSubd
		
	def cTolerance(self):
		self.cTol = float(cmds.textField(self.aTolTxt, q=True, tx=True))
		print self.cTol
		return self.cTol	

	def loadCurve(self):
		self.objToUse = cmds.ls(sl=True)
		cmds.button(self.aUSC, e=True, l=self.objToUse[0])

	def execute(self):

		sx = self.sx
		sy = self.sy
		sdv = self.sdv
		sdu = self.sdu
		tap = self.tap
		degs = self.degs
		subCurve = self.subCurve
		clean = self.clean
		do_uvs = self.do_uvs
		rbc = self.rbc
		cTol = self.cTol
		cSubd = self.cSubd
		
		if cmds.checkBox(self.aUACCB, q=True, v=True):
			useAltShape = True
		else:
			useAltShape = False
		
		multSel = cmds.ls(sl=True,fl=True, ap=True)
		if cmds.objectType(multSel[0]) == 'mesh':
			thisIsAMesh = True
		else:
			thisIsAMesh = False
		# Select curve type to extrude along - convert and store
		for x in multSel:
			print x
			if thisIsAMesh != True:
				cmds.select(x)
			else:
				cmds.select(multSel)
				
			objSel = cmds.ls(sl=True,fl=True, ap=True)
			if self.ko == 1:
				dupObj = cmds.duplicate(objSel)
				objSel = dupObj
			if len(objSel) > 1:
				print objSel
				if degs == 0:
					curveDg = cmds.promptDialog(t='Enter Degrees:', m='Enter Degrees - ie. 1 for linear, 3 for curved')
					objSel = cmds.polyToCurve(f=2, dg=int(cmds.promptDialog(q=True, tx=True)))
				else:
					objSel = cmds.polyToCurve(f=2, dg=int(degs), n='%s_curve' %objSel[0].split('.')[0])
			else:
				objType = cmds.listRelatives(objSel[0], f=True)
				if cmds.objectType(objType[0]) != 'nurbsCurve' and cmds.objectType(objType[0]) != 'bezierCurve':
				    cmds.error('Select the nurbs curve first, then the object to align')
				if cmds.objectType(objType[0]) == 'bezierCurve':
					mm.eval("bezierCurveToNurbs;")
			# Create a nurbs curve for the extrusion
			if useAltShape:
				nurbsCir = self.objToUse
			else:	
				nurbsCir = cmds.circle(n='extrudeCircle', d=3, r=1, nr=(0,0,1), sw=360, ch=True, s=8)
			objCV = cmds.ls('%s.ep[*]' %objSel[0], fl=True)
			
			noOfCV = len(objCV)
			firstCV = 0
			lastCV = noOfCV - 1
			cvNumberToUse=firstCV
			
			# Rebuild the curve to help with uniformity
			if self.rev == 1:
				cmds.reverseCurve(objSel[0], ch=0, rpo=1)
			
			if rbc == 1:
				try:
					cmds.rebuildCurve(objSel[0], ch=0,rpo=1,rt=4,end=1,kr=0, kcp=0, kep=1, kt=0, s=cSubd, d=3, tol=cTol)
					cmds.rebuildCurve(objSel[0], ch=0,rpo=1,rt=0,end=1,kr=0, kcp=0, kep=1, kt=0, s=cSubd, d=3, tol=cTol)
				except:
					cmds.warning('Tolerance for rebuild likely to low, try a higher value or turn Rebuild Curve off')
			
			if do_uvs == 1:
				objShape = cmds.listRelatives(objSel[0], c=True, type='shape')
				mInfo = cmds.shadingNode('curveInfo', n='cMeasure', asUtility=True)
				cmds.connectAttr('%s.local' %objShape[0], '%s.inputCurve' %mInfo)
				curveLength = cmds.getAttr('%s.arcLength' %mInfo)
				cmds.delete(mInfo)
				
				self.uvRatio = float((((sx * sy)*2.0) * math.pi) / curveLength)
				print "uvRatio:  " + str(self.uvRatio)
				
			
			# Create a tangent contraint to position nurbs circle to the first cv
			cvPos = cmds.xform('%s.ep[%d]' %(objSel[0],cvNumberToUse), query=True, ws=True, t=True)
			cmds.xform(nurbsCir[0], ws=True, t=(cvPos[0],cvPos[1],cvPos[2]))
			fastCon = cmds.tangentConstraint(objSel[0], nurbsCir[0], aim=(0,0,1))
			cmds.delete(fastCon[0])
			
			# Extrude along curve and set attributes
			pipeExt = cmds.extrude(nurbsCir[0], objSel[0], n='%s_pipe' %objSel[0], ch=True, rn=subCurve, po=1, et=2, ucp=1, fpt=1,upn=1, rotation=0, scale=1,rsp=1) 
			pipeTes = cmds.listConnections(pipeExt[1], type='nurbsTessellate')
			if subCurve != 0:
				pipeSubCurve = cmds.listConnections(pipeExt[1], type='subCurve')
			
			cmds.setAttr('%s.format' %pipeTes[0],2)
			cmds.setAttr('%s.polygonType' %pipeTes[0],1)
			cmds.setAttr('%s.uType' %pipeTes[0],2)
			cmds.setAttr('%s.vType' %pipeTes[0],2)
			cmds.setAttr('%s.vNumber' %pipeTes[0],sdv)
			cmds.setAttr('%s.uNumber' %pipeTes[0],sdu)
			
			# Add attributes
			if clean == 0:
				cmds.addAttr(pipeExt[0], ln='________', k=True)
				cmds.setAttr('%s.________' %pipeExt[0], l=True)
				cmds.addAttr(pipeExt[0], ln='Ext_ScaleX', k=True, dv=sx)
				cmds.addAttr(pipeExt[0], ln='Ext_ScaleY', k=True, dv=sy)
				cmds.connectAttr('%s.Ext_ScaleX' %pipeExt[0], '%s.scaleX' %nurbsCir[0])
				cmds.connectAttr('%s.Ext_ScaleY' %pipeExt[0], '%s.scaleY' %nurbsCir[0])
				cmds.addAttr(pipeExt[0], ln='Ext_DivisionV', at='short', k=True, dv=sdv)
				cmds.connectAttr('%s.Ext_DivisionV' %pipeExt[0], '%s.vNumber' %pipeTes[0])
				cmds.addAttr(pipeExt[0], ln='Ext_DivisionU', at='short', k=True, dv=sdu)
				cmds.connectAttr('%s.Ext_DivisionU' %pipeExt[0], '%s.uNumber' %pipeTes[0])
				if subCurve != 0:
					cmds.addAttr(pipeExt[0], ln='Ext_Length', k=True, dv=1, max=1, min=0)
					cmds.connectAttr('%s.Ext_Length' %pipeExt[0], '%s.maxValue' %pipeSubCurve[1])
				cmds.addAttr(pipeExt[0], ln='Ext_Taper', k=True, dv=tap, min=0)
				cmds.connectAttr('%s.Ext_Taper' %pipeExt[0], '%s.scale' %pipeExt[1])
				cmds.addAttr(pipeExt[0], ln='Ext_Twist', k=True, dv=1)
				cmds.connectAttr('%s.Ext_Twist' %pipeExt[0], '%s.rotation' %pipeExt[1])
				cmds.addAttr(pipeExt[0], ln='Ext_ComponentPivot', k=True, dv=1)
				cmds.connectAttr('%s.Ext_ComponentPivot' %pipeExt[0], '%s.useComponentPivot' %pipeExt[1])

			curveGrpNode = cmds.createNode('transform', n='pipeCurves')
			cmds.parent(nurbsCir, curveGrpNode)
			cmds.parent(objSel, curveGrpNode)
	
			cmds.setAttr('%s.inheritsTransform' %curveGrpNode, 0)
			cmds.setAttr('%s.visibility' %curveGrpNode, 1)
			cmds.parent(curveGrpNode, pipeExt[0])
			cmds.select(pipeExt[0])
			if do_uvs == 1:
				cmds.polyLayoutUV(ps=0.2)
				cmds.polyEditUV(sv=1, su=self.uvRatio)
				cmds.polyEditUV(sv=0.95, su=0.95)
				cmds.select(pipeExt[0])
				CentreUVs()
				if clean == 1:
					cmds.delete(ch=True)
					cmds.delete(curveGrpNode)
					cmds.select(pipeExt[0])
			if thisIsAMesh == True:
				print 'hello'
				break					
			#return pipeExt[0]
		
	def cleanUp(self):
		multSel = cmds.ls(sl=True)
		for x in multSel:
			cmds.select(x)
			pipeSel = cmds.ls(sl=True)
			getChild = cmds.listRelatives(pipeSel, c=True, type='transform', f=True)
			cmds.delete(ch=True)
			
			if getChild[0].split('|')[-1] == 'pipeCurves':
				cmds.delete(getChild)
			
			
			cmds.deleteAttr('%s.Ext_ScaleX' %pipeSel[0])
			cmds.deleteAttr('%s.Ext_ScaleY' %pipeSel[0])
			cmds.deleteAttr('%s.Ext_DivisionV' %pipeSel[0])
			cmds.deleteAttr('%s.Ext_DivisionU' %pipeSel[0])
			cmds.deleteAttr('%s.Ext_Taper' %pipeSel[0])
			cmds.deleteAttr('%s.Ext_Twist' %pipeSel[0])
			cmds.deleteAttr('%s.Ext_ComponentPivot' %pipeSel[0])
			cmds.setAttr('%s.________' %pipeSel[0], l=0)
			cmds.deleteAttr('%s.________' %pipeSel[0])

		cmds.select(multSel)
	
def autoPipes():
	ap = autoPipe()
	ap.autoPipeUI()