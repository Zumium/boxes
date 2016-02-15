from boxes import handlerBase

class ArchiveHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os.path
		import os
		import tarfile
		import subprocess
		import shutil
		#check numbers of argument
		if self.argumentNum != 1:
			print('usage: boxes archive BOX')
			return
		#check argument's type
		if self.arguments[0]['type'] != 'box':
			print('usage: boxes archive BOX')
			return
		#check whether it already exists as an archive
		boxName=self.arguments[0]['box']
		if self.checkArchivedBoxExists(boxName):
			print('box {} already exists as an archive'.format(boxName))
			return
		#check whether it exists
		if not self.checkBoxExists(boxName):
			print('box {} doesn\'t exist'.format(boxName))
			return
		#start to archive the box
		#first, back up the current working directory
		preCwd=os.path.abspath(os.getcwd())
		#then , change current working directory to boxes' parent foler path
		os.chdir(self.getFullBoxPath(''))
		#create archive file
		boxTarFile=tarfile.open(self.getFullArchivedBoxPath(boxName),'w:'+self.compressType)
		#unlink the box
		subprocess.call(['boxes','unlink',boxName])
		#add box to tarfile
		boxTarFile.add(boxName)
		#close tarfile
		boxTarFile.close()
		#change working directory back
		os.chdir(preCwd)
		#drop the box
		shutil.rmtree(self.getFullBoxPath(boxName))
