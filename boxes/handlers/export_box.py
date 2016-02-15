from boxes import handlerBase

class ExportHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import tarfile
		import shutil
		import os
		import os.path
		#check number of arguments
		if self.argumentNum ==0 or self.argumentNum > 2:
			print('usage: boxes export BOX [/path/to/put/archivefile]')
			return
		#check argument type
		if self.arguments[0]['type'] != 'box':
			print('usage: boxes export BOX [/path/to/put/archivefile]')
			return
		if self.argumentNum == 2:
			if self.arguments[1]['type'] != 'path':
				print('usage: boxes export BOX [/path/to/put/archivefile]')
				return
		else:
			self.arguments.append({'type':'path','path':os.getcwd()})
		#get absolute path
		self.arguments[1]['path']=os.path.abspath(self.arguments[1]['path'])
		#check whether box exists
		boxName=self.arguments[0]['box']
		if not (self.checkBoxExists(boxName) or self.checkArchivedBoxExists(boxName)):
			print('box {} doesn\'t exist'.format(boxName))
			return
		#figure out it is archived or unarchived
		isUnarchived=self.checkBoxExists(boxName)
		pathToCopyAt=self.arguments[1]['path']
		#add slash to tail
		if pathToCopyAt[-1] != self.pathSeperator:
			pathToCopyAt+=self.pathSeperator
		#start to export
		if isUnarchived:
			#it is unarchived
			#new a tar file
			boxTarFile=tarfile.open(pathToCopyAt+boxName+self.archiveTail,'w:'+self.compressType)
			#backup current working direcroty
			preCwd=os.getcwd()
			#change to boxes' parent directory
			os.chdir(self.getFullBoxPath(''))
			#add box folder to tarfile
			boxTarFile.add(boxName)
			#close tarfile
			boxTarFile.close()
			#change current working directory back
			os.chdir(preCwd)
		else:
			#it is archived
			#copy it directly out
			shutil.copy(self.getFullArchivedBoxPath(boxName),pathToCopyAt)
