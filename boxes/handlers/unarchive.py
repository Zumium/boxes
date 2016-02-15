from boxes import handlerBase

class UnarchiveHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os
		import os.path
		import tarfile
		import subprocess
		#check number of arguments
		if self.argumentNum != 1:
			print('usage: boxes unarchive BOX')
			return
		#check arugment's type
		if self.arguments[0]['type'] != 'box':
			print('usage: boxes unarchive BOX')
			return
		#check if archive exists
		archivedBoxName=self.arguments[0]['box']
		if not self.checkArchivedBoxExists(archivedBoxName):
			print('archived box {} doesn\'t exist'.format(archivedBoxName))
			return
		#start to unarchive
		#open tarfile
		boxTarFile=tarfile.open(self.getFullArchivedBoxPath(archivedBoxName),'r:'+self.compressType)
		#unarchive box
		boxTarFile.extractall(self.getFullBoxPath(''))
		#close tarfile
		boxTarFile.close()
		#remove archive file
		os.remove(self.getFullArchivedBoxPath(archivedBoxName))
		#fresh it up
		subprocess.call(['boxes','fresh',archivedBoxName])
