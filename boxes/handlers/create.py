from boxes import handlerBase

class CreateHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().init()

	def handle(self):
		import os
		#check number of arguments
		if self.argumentNum != 1:
			print('CREATE command should be followed with only one argument')
			return
		#check arugments' type
		if self.arguments[0]['type'] != 'box':
			print('CREATE command can only be followed with box name')
			return
		#check if the box already exists
		boxName=self.arguments[0]['box']
		if self.checkBoxExists(boxName):
			print('box {} already exists'.format(boxName))
			return
		elif self.checkArchivedBoxExists(boxName):
			print('box {} already exists as an archived box'.format(boxName))
			return
		#create the box
		os.mkdir(self.getFullBoxPath(boxName))
		#create specific foler
		os.mkdir(self.getBoxSpecificFolderPath(boxName))
