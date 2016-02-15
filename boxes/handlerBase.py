class BaseHandler:
	
	def __init__(self):
		import platform
		#set up memeber variables
		self.folderPath=None #unarchived boxes' path
		self.archivePath=None #archived boxes' path
		self.argumentNum=None #numbers of parameters
		self.arguments=None #parsed arguments are stored here
		self.pathSeperator='/' # '/' for UNIX-like and '\' for Windows
		self.archiveTail='.tar.gz' #compression format
		self.compressType='gz'

		#figure out current system type. UNIX or Windows?
		if platform.system() == 'Windows':
			#it's running on Windows
			self.pathSeperator='\\'

	def getLinkFilePath(self,boxName,fileName=None):
		#get hiddenf foler's path
		hiddenFolder=self.getBoxSpecificFolderPath(boxName,withSlash=True)
		if fileName == None:
			#get box link list path
			return hiddenFolder+boxName+'.boxlink'
		else:
			#get file path
			return hiddenFolder+fileName+'.link'

	def addLink(self,path,boxName,fileName=None):
		linkFile=self.getLinkFilePath(boxName,fileName)
		f=open(linkFile,'a')
		f.write(path+'\n')
		f.close()

	def getLinkList(self,boxName,fileName=None):
		linkFile=self.getLinkFilePath(boxName,fileName)
		linkList=list()
		f=open(linkFile)
		for each in f:
			linkList.append(each[:-1])
		f.close()
		return linkList

	def writeLinkList(self,linkList,boxName,fileName=None):
		linkFile=self.getLinkFilePath(boxName,fileName)
		f=open(linkFile,'w')
		for each in linkList:
			f.write(each+'\n')
		f.close()

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
 
	def checkFileExists(self,boxName,fileName):
		import os.path
		thePath=self.getFullBoxPath(boxName,withSlash=True)+fileName
		return os.path.exists(thePath)

	def getFilePath(self,boxName,fileName):
		return self.getFullBoxPath(boxName,withSlash=True)+fileName

	def putArgument(self,cmdXML):
		import xml.etree.ElementTree as ET
		import os.path
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
				newPara['path']=os.path.expanduser(x.find('path').text)
			else:
				raise NameError('No such arugment type: {}'.format(x.attrib['type']))
			self.arguments.insert(int(x.attrib['index']),newPara)

	def handle(self):
		#leave this function for blank now
		#it will be overwrited in subclasses
		pass
