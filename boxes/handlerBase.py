class BaseHandler:
	
	def init(self):
		import platform
		#set up memeber variables
		self.folderPath=None #unarchived boxes' path
		self.archivePath=None #archived boxes' path
		self.argumentNum=None #numbers of parameters
		self.arguments=None #parsed arguments are stored here
		self.pathSeperator=None # '/' for UNIX-like and '\' for Windows
		self.archiveTail='.tar.gz' #compression format

		#figure out current system type. UNIX or Windows?
		if platform.system() == 'Windows':
			#it's running on Windows
			self.pathSeperator='\\'
		else:
			#it's running on UNIX or UNIX-like
			self.pathSeperator='/'
		
	
	def setBoxPath(self,boxPath,archivePath):
		#expand ~ to user's real home path
		import os.path
		self.folderPath=os.path.expanduser(boxPath)
		self.archivePath=os.path.expanduser(archivePath)
		#add / to the end of path if they didn't
		if self.folderPath[-1] != self.pathSeperator:
			#it doesn't have. Add it on
			self.folderPath+=self.pathSeperator
		if self.archivePath[-1] != self.pathSeperator:
			#it doesn't have
			self.archivePath+=self.pathSeperator
		#check if they exist
		if not (os.path.isdir(self.folderPath) and os.path.isdir(self.archivePath)):
			raise ValueError()

	def checkBoxExists(self,boxName):
		import os.path
		boxPath=self.folderPath+boxName
		return os.path.isdir(boxPath)

	def checkArchivedBoxExists(self,boxName):
		import os.path
		boxPath=self.archivePath+boxName+self.archiveTail
		return os.path.isfile(boxPath)

	def getFullBoxPath(self,boxName,withSlash=False):
		boxPath=self.folderPath+boxName
		if withSlash:
			boxPath+=self.pathSeperator
		return boxPath

	def getFullArchivedBoxPath(self,boxName):
		return self.archivePath+boxName+self.archiveTail

	def getBoxSpecificFolderPath(self,boxName,withSlash=False):
		SpeFolder=self.getFullBoxPath(boxName,withSlash=True)+'.box'
		if withSlash:
			SpeFolder+=self.pathSeperator
		return SpeFolder
 
	def putArgument(self,cmdXML):
		import xml.etree.ElementTree as ET
		self.argumentNum=int(cmdXML.find('action').attrib['paranum'])
		self.arguments=list()
		for x in cmdXML.findall('para'):
			newPara=dict()
			if x.attrib['type'] == 'box':
				newPara['type']='box'
				newPara['box']=x.find('box').text
			elif x.attrib['type'] == 'boxfile':
				newPara['type']='boxfile'
				newPara['box']=x.find('box').text
				newPara['file']=x.find('file').text
			elif x.attrib['type'] == 'path':
				newPara['type']='path'
				newPara['path']=x.find('path').text
			else:
				raise NameError('No such arugment type: {}'.format(x.attrib['type']))
			self.arguments.insert(int(x.attrib['index']),newPara)

	def handle(self):
		#leave this function for blank now
		#it will be overwrited in subclasses
		pass
