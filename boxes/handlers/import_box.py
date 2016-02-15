from boxes import handlerBase

class ImportHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import shutil
		import os.path
		#check number of arguments
		if self.argumentNum != 1:
			print('usage: boxes import BOX_ARCHIVE_FILE_PATH')
			return
		#check argument's type
		if self.arguments[0]['type'] != 'path':
			print('usage: boxes import BOX_ARCHIVE_FILE_PATH')
			return
		#check whether file exists
		importFilePath=os.path.abspath(self.arguments[0]['path'])
		if not os.path.isfile(importFilePath):
			print('{} is not a file'.format(importFilePath))
			return
		#copy tarfile to archived boxes' directory
		shutil.copy(importFilePath,self.getFullBoxPath(''))
