from boxes import handlerBase

class CreateHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__(self)

	def handle(self):
		import os
		#check number of arguments
		if self.__argumentNum != 1:
			print('CREATE command should be followed with only one argument')
			return
		#check arugments' type
		if self.__arguments[0]['type'] != 'box':
			print('CREATE command can only be followed with box name')
			return
		#check if the box already exists
		boxName=self.__arguments[0]['box']
		if self.__checkBoxExists(boxName):
			print('box {} already exists'.format(boxName))
			return
		elif self.__checkArchivedBoxExists(boxName):
			print('box {} already exists as an archived box'.format(boxName))
			return
		#create the box
		os.mkdir(self.__getFullBoxPath(boxName))
		#create specific foler
		os.mkdir(self.__getBoxSpecificFolderPath(boxName))
