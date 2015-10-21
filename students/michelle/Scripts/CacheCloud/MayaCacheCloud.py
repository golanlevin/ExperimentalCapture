"""
*** Cache Cloud ***
Version 0.8
by Daniel Vasquez 
Updated: August 12, 2011
Email: dan@heylight.com
Web: heylight.com

Description:
Python script that creates Maya Particle Disk Cache (PDC) files from a sequence of point cloud data, and also gives you the choice of importing a single point cloud. It could be useful with all the open source data being released from Kinect hacks or 3D scanners. You can start by playing around with Radiohead's House Of Cards data: http://code.google.com/p/radiohead/downloads/list

"""
#----------------------------------------------------------------------------------------------------------------------------
import os                                                        
from struct import Struct, pack
import binascii
import maya.cmds as mc
import datetime
#----------------------------------------------------------------------------------------------------------------------------

class ArrayStructure:
    """Describes the structure of the data in the source file."""
    def __init__(self, source):
        self.source = source
        self.rawData = open(self.source, 'r').readlines() # Return file contents
        if '' in self.rawData:
            self.rawData.remove('')
        elif '\n' in self.rawData:
            self.rawData.remove('\n')
        
    def _checkNum(self, strContent):
        """Check the numerical contents of a string without changing type."""
        sC = strContent.strip()
        if sC.isdigit(): 
            return 'integer'
        else: 
            return 'float'
        
    def arrayForm(self):
        """Analysis of the form of a sample (self.arraySample) in the data. Returns a descriptive tuple: (array delimiter, array form, number of columns) """
        self.arraySample = self.rawData[len(self.rawData)//2] # Arbitrary point (median index, in this case) is used for analysis. (This analysis could probably be better done with other statistical methods.
        if self.arraySample.count(',') > 1: # Analyze comma-separated values. 
            if len(self.arraySample.split(',')) == 4:
                if self._checkNum(self.arraySample.split(',')[0]) == 'integer':
                    return 'commas',acceptableArrayforms['i3fC'], 4
                elif self._checkNum(self.arraySample.split(',')[0]) == 'float': 
                    return 'commas', acceptableArrayforms['3fiC'], 4
                else:
                    return None,acceptableArrayforms['u'], None
            elif len(self.arraySample.split(',')) == 3:
                if self._checkNum(self.arraySample.split(',')[0]) == 'float': 
                    return 'commas',acceptableArrayforms['3fC'], 3
                else:
                    return None,acceptableArrayforms['u'], None
        elif self.arraySample.count(' ') > 1: # Analyze space-separated values
            if len(self.arraySample.split(' ')) == 4:
                if self._checkNum(self.arraySample.split(' ')[0]) == 'integer':
                    return 'spaces',acceptableArrayforms['i3f'], 4
                elif self._checkNum(self.arraySample.split(' ')[0]) == 'float': 
                    return 'spaces',acceptableArrayforms['3fi'], 4
                else:
                    return None,acceptableArrayforms['u'], None
            elif len(self.arraySample.split(' ')) == 3:
                if self._checkNum(self.arraySample.split(' ')[0]) == 'float': 
                    return 'spaces',acceptableArrayforms['3f'], 3
                else:
                    return None,acceptableArrayforms['u'], None
        else:
            return None,acceptableArrayforms['u'], None
        
class ExtractData(ArrayStructure):
    """Process point cloud data for use in a Maya particle object. Create an instance by passing in the source file path."""
    def __init__(self, source): 
        """Extract data and put them in self.pointCoords and self.extraAttrValues."""
        self.pointCoords = []
        self.extraAttrValues = []
        ArrayStructure.__init__(self, source)
        arrayDelimiter = self.arrayForm()[0]
        arrayFormResult = self.arrayForm()[1]
        columnsNum = self.arrayForm()[2]
     
        for point in self.rawData:
            if arrayDelimiter == 'commas':
                pointData = point.split(',')
                if arrayFormResult == acceptableArrayforms['i3fC']:
                    pointPos = float(pointData[1]), float(pointData[2]), float(pointData[3])
                    self.pointCoords.append(pointPos)
                    self.extraAttrValues.append(float(pointData[0]))  
                elif arrayFormResult == acceptableArrayforms['3fiC']: 
                    pointPos = float(pointData[0]), float(pointData[1]), float(pointData[2])
                    self.pointCoords.append(pointPos)
                    self.extraAttrValues.append(float(pointData[3])) 
                elif arrayFormResult == acceptableArrayforms['3fC']: 
                    pointPos = float(pointData[0]), float(pointData[1]), float(pointData[2])
                    self.pointCoords.append(pointPos)
                    
            elif arrayDelimiter == 'spaces':
                pointData = point.split(' ')
                if arrayFormResult == acceptableArrayforms['i3f']:
                    pointPos = float(pointData[1]), float(pointData[2]), float(pointData[3])
                    self.pointCoords.append(pointPos)
                    self.extraAttrValues.append(float(pointData[0]))
                elif arrayFormResult == acceptableArrayforms['3fi']: 
                    pointPos = float(pointData[0]), float(pointData[1]), float(pointData[2])
                    self.pointCoords.append(pointPos)
                    self.extraAttrValues.append(float(pointData[3])) 
                elif arrayFormResult == acceptableArrayforms['3f']: 
                    pointPos = float(pointData[0]), float(pointData[1]), float(pointData[2])
                    self.pointCoords.append(pointPos)
                    
    def scaleAllpointcoords(self, factor = 1):
        """Return pointCoords scaled proportionally by factor."""
        return [(factor*coord[0], factor*coord[1], factor*coord[2]) for coord in self.pointCoords]
    def scaleXpointCoords(self, factor = 1):
        """Scale the x-coordinate by factor in each point."""
        self.pointCoords = [(factor*coord[0], coord[1], coord[2]) for coord in self.pointCoords]
    def scaleYpointCoords(self, factor = 1):
        """Scale the y-coordinate by factor in each point."""
        self.pointCoords = [(coord[0], factor*coord[1], coord[2]) for coord in self.pointCoords]
    def scaleZpointCoords(self, factor = 1):
        """Scale the z-coordinate by factor in each point."""
        self.pointCoords = [(coord[0], coord[1], factor*coord[2]) for coord in self.pointCoords]
        
    def scaleExtraAttr(self, factor = 1):
        """Return scaled self.extraAttrValues by factor for each point."""
        return [factor*v for v in self.extraAttrValues]

class PdcWriter:
    """Provides methods for processing one frame's worth of data for a single Maya particle object and outputting to binary Particle Disk Cache (.pdc) file format.
    At minimum, the 'position' data should be passed into the instance, along with the 'particleId' data. For example, instanceName = PdcWriter(position = [(0.12, 0.34, 3.67), (2.98, 0.53, 1.74)], particleId = [0,1])
    Information on the file format can be found in the Autodesk Maya documentation, under 'PDC File Format': http://download.autodesk.com/us/maya/2011help/files/PDC_File_Format_Use_the_PDC_File_Format.htm
    The packData() method uses the classes Struct and pack from Python's standard library."""
    fileType = 'PDC '
    formatVersion = 1
    byteOrder = 1
    extra1 = 0
    extra2 = 0 
    dataType = {'Integer': 0, 
                'Integer Array': 1,
                'Double': 2,
                'Double Array': 3,
                'Vector': 4, 
                'Vector Array': 5}
    headerForm = '>4sii2iii' # The default format specifier for the header
            
    def __init__(self, **data):
        self.collectedData = data
        self.attributes = self.collectedData.keys() # FIX THIS!! 
        if 'position' in data:
            self.particlesTotal = len(self.collectedData['position'])
        else: print("// Warning: Data must contain a 'position' attribute. The following was passed into the instance: {0} ".format(self.attributes))
       
    def headerValues(self):
        """Returns the default header values."""
        return (self.fileType,
                self.formatVersion,
                self.byteOrder,
                self.extra1,
                self.extra2,
                self.particlesTotal,
                len(self.attributes) )
    
    def recordsValues(self):
        """Generates records values from data. Note: Only data types Vector Array and Double Array are supported here."""
        rValues = ()
        for attr in self.attributes:
            if type(self.collectedData[attr][0]) == tuple: # If the values are tuples, then make them Vector Array...
                rValues += (len(attr), attr, self.dataType['Vector Array'])
                for v in self.collectedData[attr]:
                    rValues += v[0], v[1], v[2]
            else: # otherwise, make the values Double Array
                rValues += (len(attr), attr, self.dataType['Double Array'])
                for v in self.collectedData[attr]:
                    rValues += v,
        return rValues
        
    def recordsForm(self):
        """Generates format specifier for the records of the data. Note: Only data types Vector Array and Double Array are supported here."""
        rForm = ''
        for attr in self.attributes:
            if type(self.collectedData[attr][0]) == tuple:
                rForm +='i{0}si{1}d'.format(len(attr), 3*len(self.collectedData[attr]))
            else:
                rForm +='i{0}si{1}d'.format(len(attr), len(self.collectedData[attr]))
        
        return rForm
    
    
    def packData(self):
        """Packs data that is to be written to a binary file."""
        form = Struct(self.headerForm + self.recordsForm())
        allValues = self.headerValues() + self.recordsValues()
        return form.pack(*allValues)
    

    def hexbytes(self):
        """Converts to a sequence of hex bytes."""
        bindata = self.packData()
        return binascii.hexlify(bindata)

class PdcFileStep:
    """Provides methods for setting up the appropriate naming convention of PDC files. The step number in the names of PDC files depends on the frame rate of the animation. See self.displayunits() for the list of timeunit/filestep pairs."""
    filesteps = [('pal', 240), ('ntsc', 200), ('film', 250), ('palf', 120), ('ntscf', 100), ('show', 125), ('millisec', None), ('sec', None), ('min', None), ('hour', None), ('2fps', None), ('3fps', None), ('4fps', None), ('5fps', None), ('6fps', None), ('8fps', None), ('10fps', None), ('12fps', None), ('16fps', None), ('20fps', None), ('40fps', None), ('75fps', None), ('80fps', None), ('100fps', None), ('120fps', None), ('125fps', None), ('150fps', None), ('200fps', None), ('240fps', None), ('250fps', None), ('300fps', None), ('375fps', None), ('400fps', None), ('500fps', None), ('600fps', None), ('750fps', None), ('1000fps', None), ('1200fps', None), ('1500fps', None), ('2000fps', None), ('3000fps', None), ('6000fps', None)]
    stepdict = dict(filesteps)
    
    def __init__(self, timeunit):
        self.timeunit = timeunit
        
        if type(self.timeunit) == str:
            if self.stepdict[self.timeunit] == None:
                print('// Warning: The time unit {0} does not yet have a corresponding file step number. Set it with method self.setfilestep().\n'.format(self.timeunit))
            else:
                self.filestep = self.stepdict[self.timeunit]
        else:
            print('// Warning: Argument must be a string specifying the working time unit. For a list of available time units, execute the method self.displayunits()')
    
    def pdcfilestep(self):
        if self.stepdict[self.timeunit] == None:
            print('// A file step has not been specified for time unit "{0}". Set it with method self.setfilestep(time unit, file step).\n'.format(self.timeunit))
        else:
            return self.stepdict[self.timeunit]
        
    def displayunits(self):
        header = '(Time unit, File step)'
        print('-'*len(header))
        print(header)
        print('-'*len(header))
        l = [(unit, self.stepdict[unit]) for unit in self.stepdict.keys()]
        l.sort()
        l.reverse()
        #print(l)
        for unit in l:
            print(unit[0], unit[1])
        print('\nIf file step is None, must set it with method self.setfilestep().\n')

    def setfilestep(self,timeunit, filestep):
        if timeunit not in self.stepdict.keys():
            print('// "{0}" is not a valid time unit; must use Maya-specific time unit. See self.displayunits() for list and try again.'.format(timeunit))
        else:
            self.timeunit = timeunit
            d = self.stepdict
            d.update(dict([(timeunit, filestep)]))
            print('// Time unit "{0}" has been set up to correspond to a file step of {1}.'.format(self.timeunit, self.stepdict[self.timeunit]))
    
def exitPrompt():
    surePrompt = mc.confirmDialog( icn = 'warning', title='Leaving Cache Cloud...', message='Sure you want to stop here?', button=['Go Back','Stop'], defaultButton='Go Back', cancelButton='Stop', dismissString='Stop' )
    if surePrompt == 'Go Back':
        return True
    else:
        print("*** Goodbye.")
        #historyLog.write('{0}\n\n\n'.format((datetime.datetime.now()).strftime("SESSIONEND\tNo particles created. User exited: %Y-%m-%d %H:%M:%S")))
        return False
### Initiate-------------------------------------------------------------------------------------------------------------------
versionNum = '0.9.0'
print('*** Welcome to Cache Cloud version {0} ***'.format(versionNum))
# Prepare the directory for particle disk cache (PDC) files
projectrootDir = str(mc.workspace(q=1,rootDirectory=1)) 
particlesDir =  projectrootDir + 'particles/'
if os.path.isfile(particlesDir + 'CacheCloud_history.txt'): # Record session in history log
    historyLog = open(particlesDir + 'CacheCloud_history.txt', 'a') # If file exists, append write
else:
    historyLog = open(particlesDir + 'CacheCloud_history.txt', 'w') # If file doesn't exist, create new and write
    historyLog.write('{0} Cache Cloud {1} {2}\n'.format('*'*6, versionNum,'*'*6 )) # Write title and general info
    historyLog.write('Written by Daniel Vasquez\nEmail: dan@heylight.com\n\n')
    historyLog.write('History log:\n\n')
acceptableArrayforms = {'i3fC': 'int, float, float, float',
                            '3fiC': 'float, float, float, int',
                            '3fC': 'float, float, float', 
                            'i3f': 'int float float float',
                            '3fi': 'float float float int',
                            '3f':'float float float',
                            'u': 'unknown'}

cleanPrompt = None
surePrompt = True
### Choose import type and select file(s)
while surePrompt:
    importChoice = mc.confirmDialog(icn='information',title='Welcome to Cache Cloud!',message="Create PDC files from a point cloud animation or\nimport point cloud single.",button=['Animation', 'Single', 'Cancel'],defaultButton='Animation',cancelButton='Cancel',dismissString='Cancel')
    if importChoice == 'Animation':
        sourceFiles = mc.fileDialog2(fm=4, ds = 2, okc = 'Select', cap = 'Select the first file in the point cloud animation or a range of files') 
        try:
            sourceFiles.sort() # Sort files in order - important for timeslider range
        except: AttributeError
        if sourceFiles == None:
            surePrompt = exitPrompt()
        else:
            break   
    elif importChoice == 'Single':
        sourceFiles = mc.fileDialog2(fm=1, ds = 2, okc = 'Select', cap = 'Select a point cloud data file')
        if sourceFiles == None:
            surePrompt = exitPrompt()
        else:
            break   
    else:
        surePrompt = exitPrompt()    
if importChoice == 'Animation':
    while surePrompt:
        result = mc.promptDialog(title='New scene',message='Name the scene for your point cloud animation:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
        if result == 'OK':
            sceneName = mc.promptDialog(query=True, text=True)
            break
        elif result == 'Cancel':
            surePrompt = exitPrompt()
    while surePrompt:
        timeUnits = {'25 fps': 'pal', '60 fps': 'ntscf', '30 fps': 'ntsc', '50 fps': 'palf', '24 fps': 'film', '15 fps': 'game', '48 fps': 'show', 'Other': 'Next', 'Not sure': 'ntsc'}
        frameRate = timeUnits[mc.confirmDialog(icn = 'question', title='Set time unit',message = 'choose frame rate:', button=['30 fps','25 fps', 'Other'],defaultButton='30 fps',cancelButton='30 fps',dismissString='30 fps')] # Choose a frame rate. To do: Get rid of text field.
        if frameRate != 'Next':
            print('*** Frame rate has been set to {0}.'.format(frameRate))
        elif frameRate == 'Next':
            frameRate = timeUnits[mc.confirmDialog(icn = 'question', title='Set time unit',message = 'choose frame rate:', button=['24 fps', '60 fps', '50 fps', '48 fps', 'Not sure'],defaultButton='Not sure',cancelButton='Not sure',dismissString='Not sure')] # Choose a frame rate. To do: Get rid of text field.
            print('*** Frame rate has been set to {0}.'.format(frameRate))
        # Give save current scene options
        try:
            mc.file(new=1)
            mc.file(rename=sceneName)
            mc.file(save=1, type='mayaAscii') # Only saves as .ma file
            mc.currentUnit(time = frameRate) # 
            break
        except RuntimeError:
            savePrompt = mc.confirmDialog(icn = 'warning',title='Create new scene:', message='Save and close the current scene?', button=['Save','Save As','Don\'t Save', 'Cancel'], defaultButton='Save', cancelButton='Cancel', dismissString='Cancel' )
            if savePrompt == 'Save':
                nameSavedscene = str(mc.file(q=1,sceneName=1, shortName=1))
                mc.file(save=1)
                print('*** The following was saved and closed: "{0}" '.format(nameSavedscene))
                mc.file(new=1)
                mc.file(rename=sceneName)
                mc.file(save=1, type='mayaAscii')
                mc.currentUnit(time = frameRate)
                print('*** New scene "{0}.ma" was created. '.format(sceneName))
                break
            elif savePrompt == 'Save As':
                chosenFile = mc.fileDialog2()[0]
                mc.file(rename = chosenFile)
                mc.file(save=1)  # To do: When replacing an .ma file with a .mb file. Unable to reopen it after. // Error: Error reading file. //  
                print('*** The following was saved and closed: "{0}" '.format(chosenFile))
                mc.file(new=1)
                mc.file(rename=sceneName)
                mc.file(save=1, type='mayaAscii')
                mc.currentUnit(time = frameRate)
                print('*** New scene "{0}.ma" was created. '.format(sceneName))
                break
            elif savePrompt == 'Don\'t Save': 
                mc.file(new=1, f=1)
                mc.file(rename=sceneName)
                mc.file(save=1, type='mayaAscii')
                mc.currentUnit(time = frameRate)
                print('*** New scene "{0}.ma" was created. '.format(sceneName))
                break
            elif savePrompt == 'Cancel':
                surePrompt = exitPrompt()
    #---------------------------------------------------------------------------------------------- -------------------     
    ### Prepare the directory for particle disk cache (PDC) files
    sceneNameWithExt = str(mc.file(q=1,sceneName=1, shortName=1))
    sceneName = sceneNameWithExt.split('.')[0] # Re-assign sceneName with current scene name, just to be sure. (Also good to have for script updates.)
    cacheoutputDir = particlesDir + sceneName + '/'
    #print("particlesDir = '{0}' \ncacheoutputDir = '{1}' \nsceneName = '{2}'".format(particlesDir, cacheoutputDir, sceneName))
    while surePrompt:
        if os.path.exists(particlesDir): # If particles folder exists. 
            createDirPrompt = mc.confirmDialog( title='Prepare folder for PDC files:', message='The following folder will be created in the particles directory of your project:\n /{0} '.format(sceneName), button=['Okay','Stop'], defaultButton='Okay', cancelButton='Stop', dismissString='Stop' )
            if createDirPrompt == 'Okay':
                if os.path.exists(cacheoutputDir):
                    print('*** The folder /{0} already exists and was not overwritten. '.format(sceneName))
                    break # If cache folder with same name already exists, skip folder creation.
                os.makedirs(cacheoutputDir)
                print('*** The folder /{0} was created in your project workspace. '.format(sceneName))
                break
            else:
                surePrompt = exitPrompt()
        else:
            createDirPrompt = mc.confirmDialog( title='Preparing folders for PDC files:', message='The following folders will be created in the directory of the current project:\n /{0}/{1} '.format('particles',sceneName), button=['Okay','Stop'], defaultButton='Okay', cancelButton='Stop', dismissString='Stop' )
            if createDirPrompt == 'Okay':
                os.makedirs(cacheoutputDir)
                print('*** The folders /{0} was created in your project workspace. '.format(cacheoutputDir))
                break
            else: # Exit prompt
                surePrompt = exitPrompt()
    ### Create particle object at first frame and make initial cache
    while surePrompt:
        particlenamePrompt = mc.promptDialog(title='Create particle',message='Name the particle object:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
        if particlenamePrompt == 'OK':
            particlesName = mc.promptDialog(query=True, text=True)
            if particlesName == '':
                particlenamePrompt = mc.confirmDialog( icn = 'warning', title='Careful...', message='No particle name was entered', button=['Try Again'], defaultButton='Try Again', cancelButton='Try Again', dismissString='Try Again' )
            else:
                mc.particle(name=particlesName)
                mc.file(save=1)
                # Get shape name of particle object. This name will be used for naming the PDC files.
                pdcBasename = mc.particle(q=1,n=1) # Get particle shape name. The following command is much faster: mc.particle(q=1,n=1)
                #[n for n in mc.ls(shapes=1) if n.startswith(''.join(i for i in particlesName if not i.isdigit()))][0]
                print('*** Particle "{0}" was created. '.format(particlesName))
                break
        elif particlenamePrompt == 'Cancel':
            surePrompt = exitPrompt()
    while surePrompt:
        ### Make a list of the source files and analyze data structure to clean up
        #Extract information from the first file
        if len(sourceFiles) == 1: # If only one file was selected, use all relevant files in the directory. Otherwise, keep sourceFiles as is.
            namePrefix = ( ''.join(i for i in os.path.split(sourceFiles[0])[1] if not i.isdigit()) ).split('.')[0] # Get the prefix name
            firstFrame = int(''.join(i for i in os.path.split(sourceFiles[0])[1] if i.isdigit()))
            #sourcefileDir = os.path.split(sourceFiles[0])[0] # This is just in case someone gets confused with the expression below to re-assign sourceFiles. (No idea how I managed this one. Basically, it makes a list of all the files in the remaining sequence with the same prefix name.)
            sourceFiles = [(os.path.split(sourceFiles[0])[0] + '/' + f)  # Selected directory + f
                             for f in os.listdir(os.path.split(sourceFiles[0])[0]) # Make list: For f in [all files in selected directory]
                             if f.startswith(namePrefix) and # Only if f starts with the same namePrefix
                             os.path.isfile(os.path.split(sourceFiles[0])[0] + '/' + f) and # and if f is an actual file 
                             firstFrame <= int(''.join(i for i in f if i.isdigit())) ] # and if f is greater than the selected file. 
            inFile = ExtractData(sourceFiles[0])
            print('*** Single file in the data sequence was selected. Using all files in same sequence.')
            # Clean up some points
            zerosCount = len([x for x in inFile.pointCoords if sum(x) ==0]) # Get the offset of every zero-value point  
            if zerosCount > 0:     
                cleanPrompt = mc.confirmDialog(icn = 'warning', title='Clean Up', message='After looking at the data in "{1}", {0} points were found to have zero-value.\nRemove all zero-value points?'.format(zerosCount, os.path.split(sourceFiles[0])[1]), button=['Remove','Keep'], defaultButton='Keep', cancelButton='Keep', dismissString='Keep' )
                if cleanPrompt == 'Remove':
                    print('*** {0} zero-value points will be removed.'.format(zerosCount))
                else:
                    print('*** There are zero-values that will not be removed.')
            sourceDir= os.path.split(sourceFiles[0])[0] + '/'
        elif len(sourceFiles) > 1: # Keep sourceFiles as is.
            namePrefix = ( ''.join(i for i in os.path.split(sourceFiles[0])[1] if not i.isdigit()) ).split('.')[0] # Get the prefix name
            print('*** A range of files in the data sequence was selected.') # If a range of files was selected, use those files only
            inFile = ExtractData(sourceFiles[0])
             # Clean up some points
            zerosCount = len([x for x in inFile.pointCoords if sum(x) ==0])  # Get the offset of every zero-value point   
            if zerosCount > 0:  
                cleanPrompt = mc.confirmDialog(icn = 'warning', title='Clean Up', message='After looking at the data in "{1}", {0} points were found to have zero-value.\nRemove all zero-value points?'.format(zerosCount, os.path.split(sourceFiles[0])[1]), button=['Remove','Keep'], defaultButton='Keep', cancelButton='Keep', dismissString='Keep' )
                if cleanPrompt == 'Remove':
                    print('*** Zero-value points will be removed.')
                else:
                    print('*** There are zero-values that will not be removed.')
            sourceDir= os.path.split(sourceFiles[0])[0] + '/'
            firstFrame = int(''.join(i for i in os.path.split(sourceFiles[0])[1]if i.isdigit()))
        fileExt = '.' + ( ''.join(i for i in os.path.split(sourceFiles[0])[1] if not i.isdigit()) ).split('.')[1]    # File extension
        ### Set up timeslider depending on number of source files (i.e. sourceFiles). (This section is questionable and might not even be necessary.)
        framesCount = len(sourceFiles)  
        startFrame = mc.playbackOptions(e=1, ast= firstFrame)
        endFrame = mc.playbackOptions(e=1, animationEndTime = firstFrame + framesCount - 1)
        mc.playbackOptions(e=1, min=startFrame)
        mc.playbackOptions(e=1, max=endFrame)  # The minus 2 buffer is a temporary fix to the issue of Maya crashing at the last frame.
        mc.currentTime(startFrame)
        # Create a default particle disk cache (which will be overwritten)
        mc.dynExport( particlesName, path = sceneName,  f = 'cache', mnf = firstFrame, mxf = endFrame, oup = 0)
    #-----------------------------------------------------------------------------------------------------------------     
        
        if inFile.arrayForm()[2] == 4:
            print('*** The following form of array was detected: {0}'.format(inFile.arrayForm()[1]))
            extraAttr = mc.confirmDialog( title='Extra attribute', message='There was an extra integer value detected in the arrays. Assign it to an attribute?', button=['radiusPP','opacityPP', 'rotationPP', 'SKIP' ], defaultButton='SKIP', cancelButton='SKIP', dismissString='SKIP' )
            avgAttrvalues = sum(inFile.extraAttrValues)/len(inFile.extraAttrValues)
            maxAttrValue = max(inFile.extraAttrValues)
            #minAttrValue = min(extraAttrValues)
            if extraAttr == 'SKIP': # If no attribute was chosen , make the arrayLength = 3
                arrayLength = 3
            else:
                while surePrompt:
                    scalefactorPrompt = mc.promptDialog(title='Scale attribute',text = '{0}'.format(str(1/maxAttrValue)),message='The highest value of {0} is {2}. The average value is {1:.2f}.\n Scale it by:'.format(extraAttr,avgAttrvalues, maxAttrValue),button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
                    if scalefactorPrompt == 'OK':
                        extraScalefactor = mc.promptDialog(query=True, text=True)
                        if extraScalefactor == '':
                            mc.confirmDialog( icn = 'warning', title='Careful...', message='No scale value was entered', button=['Try Again'], defaultButton='Try Again', cancelButton='Try Again', dismissString='Try Again' )
                        else:
                            print('*** A multiplication factor of {0} will be applied to {1} values. '.format(extraScalefactor, extraAttr))
                            break
                    elif scalefactorPrompt == 'Cancel':
                        surePrompt = exitPrompt()
                print('*** The extra integer value has been assigned to the attribute: {0}.'.format(extraAttr))  
                arrayLength = inFile.arrayForm()[2] # This should reference to 4
        else:
            arrayLength = inFile.arrayForm()[2] # This should reference to 3
            print('*** The following form of array was detected: {0}'.format(inFile.arrayForm()[1]))
        print('*** Beginning to write PDC files. This may take some time...')
        print(datetime.datetime.now()).strftime("*** Started: %Y-%m-%d %H:%M:%S")
        historyLog.write('{0}\n'.format((datetime.datetime.now()).strftime("SESSIONSTART    Started creating PDC files: %Y-%m-%d %H:%M:%S")))
        historyLog.write('INPUT\t{0} files ({3}) with root name "{1}" from {2}\n'.format(str(len(sourceFiles)),namePrefix,sourceDir,fileExt))
    #-----------------------------------------------------------------------------------------------------------------     
        ### This is where it all the magic happens! Writing the PDC files in binary...
        # This is important for naming the PDC files in a Maya-specific incremental value
        step = PdcFileStep(frameRate)
        pdcNameIncrementsValue = step.pdcfilestep()
        pdcIncrements = firstFrame * pdcNameIncrementsValue
        writtenPDCCount = 0 # Loop for each file to make a PDC file.
        for sourcefile in sourceFiles:
            pc = ExtractData(sourcefile)
            particleIds = range(len(pc.pointCoords)) 
            
            if cleanPrompt == 'Remove': # Clean up zero-point values if user chose 'Remove' in cleanPrompt above
                particleIds = [pc.pointCoords.index(x) for x in pc.pointCoords if sum(x) != 0] # Collect offsets that correspond to nonzero-value points to use as particleIds
                historyLog.write('OUTPUT\t{1} points were removed from {0}\n'.format(os.path.split(sourcefile)[1],len([x for x in pc.pointCoords if sum(x) == 0]))) 
                pc.pointCoords = [x for x in pc.pointCoords if sum(x) !=0] # Filter out all zero-value pointsparticlesTotal = len(pointCoords)
            if arrayLength == 4:
                extraAttrValuesR = []
                [extraAttrValuesR.append(pc.extraAttrValues[i]*float(extraScalefactor)) for i in particleIds]
                pc.extraAttrValues = extraAttrValuesR
                
            # Pack the binary data into the PDC files
                bindata = PdcWriter(position = pc.pointCoords, particleId = particleIds) 
                bindata.collectedData[extraAttr] = pc.extraAttrValues # Append the extra attribute extraAttr and its values to the dictionary self.collectedData 
                bindata.attributes += [str(extraAttr)]# Append the extra attribute to the list self.attributes
              
            else:
                bindata = PdcWriter(position = pc.pointCoords, particleId = particleIds)

            fileName = pdcBasename + '.' + str(pdcIncrements) + ".pdc"
            outputPDCfile = open(cacheoutputDir + fileName, 'wb')
            print('// Writing PDC file from {0}: {1}'.format(os.path.split(sourcefile)[1], cacheoutputDir + fileName) )
            outputPDCfile.write(bindata.packData())
            outputPDCfile.close()
            #historyLog.write('OUTPUT    Source file {0}: {1}\n'.format(os.path.split(sourcefile)[1], cacheoutputDir + fileName) )
            pdcIncrements += pdcNameIncrementsValue     # Add value according to frameRate
            writtenPDCCount  += 1
        break    
    if surePrompt:
        historyLog.write('OUTPUT\t{0} PDC files have been written to {1}\n'.format(str(writtenPDCCount),cacheoutputDir))
        #historyLog.write('HEADER\tType = {0}\nHEADER\tFormat version = {1}\nHEADER\tByte order = {2}\nHEADER\tExtra1 = {3}\nHEADER\tExtra2 = {4}\n'.format(fileType,formatVersion, byteOrder,extra1,extra2))
        historyLog.write('RECORDS\tTotal points = {0}\nRECORDS\tAttributes assigned = {1}\n'.format(len(pc.pointCoords),bindata.attributes))
        historyLog.write('{0}\n\n\n'.format((datetime.datetime.now()).strftime("SESSIONEND\tPDC files completed: %Y-%m-%d %H:%M:%S")))
        print('*** Your particle disk cache has been created. Thanks for using Cache Cloud!\n\n')
        finalPrompt = mc.confirmDialog(title='Done.', message='Your particle disk cache has been created.\nThanks for using Cache Cloud!', button=['Close','Heylight.com'], defaultButton='Close', cancelButton='Close', dismissString='Close' )
        if finalPrompt == 'Close':
            historyLog.close()
            mc.currentTime(startFrame)
            #mc.addAttr (-ln goalWeight0PP0 -dt doubleArray drtfhShape
        else:
            historyLog.close()
            mc.currentTime(startFrame)
            import webbrowser 
            webbrowser.open('http://folio.heylight.com/#953120/Info')
        surePrompt = False
    elif surePrompt == False:
        finalPrompt = mc.confirmDialog(title='Exit', message='Your particle disk cache has not been created. Thanks for using Cache Cloud anyway!', button=['Close'], defaultButton='Close', cancelButton='Close', dismissString='Close' )    

### If importing a single point cloud ---------------------------------------------------------------------------------------------------------------- 
elif importChoice == 'Single':
    inFile = ExtractData(sourceFiles[0])# Instantiate file object, which collects pointCoords and extraAttrValues data

    if inFile.arrayForm()[1] == 'unknown':
        abortPrompt = mc.confirmDialog(title='Aborting', message='An {0} form of array was detected. Aborting Cache Cloud.'.format(inFile.arrayForm()[1]), button=['Close'], defaultButton='Close', cancelButton='Close', dismissString='Close' )    
        print('*** An {0} form of array was detected. Aborted Cache Cloud.'.format(inFile.arrayForm()[1]))
        surePrompt = False
    print(datetime.datetime.now()).strftime("// Started: %Y-%m-%d %H:%M:%S")
    historyLog.write('{0}\n'.format((datetime.datetime.now()).strftime("SESSIONSTART\tCreated single point cloud: %Y-%m-%d %H:%M:%S")))
     
    particleIds = range(len(inFile.pointCoords)) 
    #if surePrompt: # I think this surePrompt is totally unnecessary. Remove later, and test.
    zerosCount = len([x for x in inFile.pointCoords if sum(x) ==0])  # Get the offset of every zero-value point   
    if zerosCount > 0:  
        cleanPrompt = mc.confirmDialog(icn = 'warning', title='Clean Up', message='After looking at the data in "{1}", {0} points were found to have zero-value.\nRemove all zero-value points?'.format(zerosCount, os.path.split(sourceFiles[0])[1]), button=['Remove','Keep'], defaultButton='Keep', cancelButton='Keep', dismissString='Keep' )
        if cleanPrompt == 'Remove':
            print('*** Zero-value points will be removed.')
        else:
            print('*** There are zero-values that will not be removed.')
    historyLog.write('INPUT\tSingle point-cloud data file: {0}\n'.format(str(sourceFiles[0])))
    if inFile.arrayForm()[2] == 4:
        print('*** The following form of array was detected: {0}'.format(inFile.arrayForm()[1]))
        extraAttr = mc.confirmDialog( title='Extra attribute', message='There was an extra integer value detected in the arrays. Assign it to an attribute?', button=['radiusPP','opacityPP', 'mass', 'SKIP' ], defaultButton='SKIP', cancelButton='SKIP', dismissString='SKIP' )
        maxAttrValue = max(inFile.extraAttrValues)
        avgAttrvalues = sum(inFile.extraAttrValues)/len(inFile.extraAttrValues)
        if extraAttr == 'SKIP': # If no attribute was chosen , make the arrayLength = 3
            arrayLength = 3
        else:
            while surePrompt:
                scalefactorPrompt = mc.promptDialog(title='Scale attribute',text = '{0}'.format(str(1/maxAttrValue)),message='The highest value of {0} is {2}. The average value is {1:.2f}.\n Scale it by:'.format(extraAttr,avgAttrvalues, maxAttrValue),button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
                if scalefactorPrompt == 'OK':
                    extraScalefactor = mc.promptDialog(query=True, text=True)
                    if extraScalefactor == '':
                        mc.confirmDialog( icn = 'warning', title='Careful...', message='No scale value was entered', button=['Try Again'], defaultButton='Try Again', cancelButton='Try Again', dismissString='Try Again' )
                    else:
                        print('*** A multiplication factor of {0} will be applied to {1} values. '.format(extraScalefactor, extraAttr))
                        break
                elif scalefactorPrompt == 'Cancel':
                    surePrompt = exitPrompt()
            print('*** The extra integer value has been assigned to the attribute: {0}.'.format(extraAttr))  
            arrayLength = inFile.arrayForm()[2] # This should reference to 4
    else:
        arrayLength = inFile.arrayForm()[2] # This should reference to 3
        print('*** The following form of array was detected: {0}'.format(inFile.arrayForm()[1]))
    if cleanPrompt == 'Remove': # Clean up zero-point values if user chose 'Remove' in cleanPrompt above
        particleIds = [inFile.pointCoords.index(x) for x in inFile.pointCoords if sum(x) !=0] # Collect offsets that correspond to nonzero-value points to use as particleIds
        #print('///{1} points were removed from {0}'.format(os.path.split(sourcefile)[1],len([pointCoords.index(x) for x in pointCoords if sum(x) ==0]))) 
        historyLog.write('OUTPUT\t{1} points were removed from data in {0}\n'.format(os.path.split(sourceFiles[0])[1],len([x for x in inFile.pointCoords if sum(x) == 0]))) 
        inFile.pointCoords = [x for x in inFile.pointCoords if sum(x) !=0] # Filter out all zero-value pointsparticlesTotal = len(inFile.pointCoords)
    mc.particle(n= os.path.split(sourceFiles[0])[1].split('.')[0]+'particle',position = inFile.pointCoords)# create particles with same name as source file
    attributes = ['position','particleId']
    if arrayLength == 4:
        attributes = [str(extraAttr)] + attributes
        extraAttrValuesR = []
        [extraAttrValuesR.append(inFile.extraAttrValues[i]*float(extraScalefactor)) for i in particleIds]
        inFile.extraAttrValues = extraAttrValuesR
        mc.addAttr(mc.particle(q=1,n=1),ln=extraAttr, dt='doubleArray') # Add the extraAttr to the particle object
        mc.addAttr(mc.particle(q=1,n=1),ln=extraAttr+'0', dt='doubleArray') # Add the extraAttr to the particle object
        [mc.particle(e=1, at = extraAttr, id=i, fv = v) for i, v in enumerate(inFile.extraAttrValues)] # Edit the values corresponding to extraAttrValues for each particle
    historyLog.write('OUTPUT\tTotal points = {0}\nOUTPUT\tAttributes assigned = {1}\n'.format(str(len(inFile.pointCoords)),attributes))
    historyLog.write('OUTPUT\tNo cache was created for single frame\n')    
    historyLog.write('{0}\n\n\n'.format((datetime.datetime.now()).strftime("SESSIONEND\tImport completed: %Y-%m-%d %H:%M:%S")))
    print(datetime.datetime.now()).strftime("// Completed: %Y-%m-%d %H:%M:%S")
    print('*** Your point cloud has been imported. Thanks for using Cache Cloud!\n')
    finalPrompt = mc.confirmDialog(title='Done.', message='Your particles have been created.\nThanks for using Cache Cloud!', button=['Close','Heylight.com'], defaultButton='Close', cancelButton='Close', dismissString='Close' )
    if finalPrompt == 'Close':
        historyLog.close()
    elif finalPrompt == 'Heylight.com':
        historyLog.close()
        import webbrowser 
        webbrowser.open('http://folio.heylight.com/#953120/Info')
    else: pass
elif surePrompt == False:
    finalPrompt = mc.confirmDialog(title='Exit', message='Thanks for using Cache Cloud anyway!', button=['Close'], defaultButton='Close', cancelButton='Close', dismissString='Close' )     
