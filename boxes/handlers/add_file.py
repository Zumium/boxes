from boxes import handlerBase

class AddFileHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os.path
		import shutil
		#check arguments' number
		if self.argumentNum != 2:
			print('ADD command should be followed with 2 arguments')
			return
		#check argument type
		if self.arguments[0]['type'] != 'box' or self.arguments[1]['type'] != 'path':
			print('usage: boxes add BOX_NAME /path/to/file')
			return
		#check if box exists
		if self.checkBoxExists(self.arguments[0]['box']):
			print('box {} doesn\'t exist'.format(self.arguments[0]['box']))
			return
		#check if path exists
		if os.path.exists(self.arguments[1]['path']):
			print('{} doesn\'t exist'.format(self.arguments[1]['path']))
			return
		#figure out path is file or directory
		isDir=os.path.isdir(self.arguments[1]['path'])
		if isDir:
			#is a directory
			#get directory's name
			dirName=None
			dirPath=self.arguments[1]['path']
			pathSplit=dirPath.split(self.pathSeperator)
			if pathSplit[-1] == '':
				dirName=pathSplit[-2]
			else:
				dirName=pathSplit[-1]
			newDirPath=self.getFullBoxPath(self.arguments[0]['box'],withSlash=True)+dirName
			shutil.copytree(dirPath,newDirPath)
		else:
			#is a file
			shutil.copy(self.arguments[1]['path'],self.getFullBoxPath(self.arguments[0]['box']))
