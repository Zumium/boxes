class BaseHandler:
	
	def __init__(self):
		import platform
		#set up memeber variables
		self.__folderPath=None #unarchived boxes' path
		self.__archivePath=None #archived boxes' path
		self.__argumentNum=None #numbers of parameters
		self.__arguments=None #parsed arguments are stored here
		self.__pathSeperator=None # '/' for UNIX-like and '\' for Windows
		self.__archiveTail='.tar.gz' #compression format

		#figure out current system type. UNIX or Windows?
		if platform.system() == 'Windows':
			#it's running on Windows
			self.__pathSeperator='\\'
		else:
			#it's running on UNIX or UNIX-like
			self.__pathSeperator='/'
		
	
	def setBoxPath(self,boxPath,archivePath):
		#expand ~ to user's real home path
		import os.path
		self.__folderPath=os.path.expanduser(boxPath)
		self.__archivePath=os.path.expanduser(archivePath)
		#add / to the end of path if they didn't
		if self.__folderPath[-1] != self.__pathSeperator:
			#it doesn't have. Add it on
			self.__folderPath+=self.__pathSeperator
		if self.__archivePath[-1] != self.__pathSeperator:
			#it doesn't have
			self.__archivePath+=self.__pathSeperator
		#check if they exist
		if not (os.path.isdir(self.__folderPath) and os.path.isdir(self.__archivePath)):
			raise ValueError()

	def __checkBoxExists(self,boxName):
		import os.path
		boxPath=self.__folderPath+boxName
		return os.path.isdir(boxPath)

	def __checkArchivedBoxExists(self,boxName):
		import os.path
		boxPath=self.__archivePath+boxName+self.__archiveTail
		return os.path.isfile(boxPath)

	def __getFullBoxPath(self,boxName,withSlash=False):
		boxPath=self.__folderPath+boxName
		if withSlash:
			boxPath+=self.__pathSeperator
		return boxPath

	def __getFullArchivedBoxPath(self,boxName):
		return self.__archivePath+boxName+self.__archiveTail

	def putArgument(self,cmdXML):
		import xml.etree.ElementTree as ET
		self.__argumentNum=int(cmdXML.find('action').attrib['paranum'])
		self.__arguments=list()
		for x in cmdXML.findall('para'):
			newPara=dict()
			if x.attrib['type'] == 'box':
				newPara['type']='box'
				newPara['box']=x.find('box').text
			elif x.attrib['type'] == 'boxfile':
				newPara['type']='boxfile':
				newPara['box']=x.find('box').text
				newPara['file']=x.find('file').text
			elif x.attrib['type'] == 'path':
				newPara['type']='path'
				newPara['path']=x.find('path').text
			else:
				raise NameError('No such arugment type: {}'.format(x.attrib['type']))
			self.__arguments.insert(int(x.attrib['index']),newPara)

	def handle():
		#leave this function for blank now
		#it will be overwrited in subclasses
		pass
