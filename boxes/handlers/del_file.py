from boxes import handlerBase

class DelFileHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os
		import shutil
		import os.path
		import subprocess
		#check number of argument
		if self.argumentNum != 1:
			print('DEL command should be followed with only 1 argument')
			return
		#chekc type of argument
		if self.arguments[0]['type'] != 'boxfile':
			print('DEL command should be with specified box and file name')
			return
		#get path of the file to be deleted
		boxName=self.arguments[0]['box']
		fileName=self.arguments[0]['file']
		delPath=self.getFullBoxPath(boxName,withSlash=True)+fileName
		#check if file exists
		if not self.checkFileExists(boxName,fileName):
			print('{0} in box {1} doesn\'t exist'.format(fileName,boxName))
			return
		#is delPath directory or file?
		isDir=os.path.isdir(delPath)
		#operation comfirm
		print('Are you sure to delete {0} in box {1}'.format(fileName,boxName))
		print('The file will be lost permanently if you confirm(y/n)')
		answer=input()
		if answer == 'y':
			subprocess.call(['boxes','unlink',boxName+':'+fileName])
			if isDir:
				shutil.rmtree(delPath)
			else:
				os.remove(delPath)
		else:
			print('Operation cancelled')
