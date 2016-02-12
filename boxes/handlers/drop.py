from boxes import handlerBase

class DropHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import shutil
		import os
		#check number of arguments
		if self.argumentNum != 1:
			print('DROP command should be followed with only one argument')
			return
		#check argument type
		if self.arguments[0]['type'] != 'box':
			print('DROP command can be only followed by box name')
			return
		#get box name
		boxName=self.arguments[0]['box']
		#check if the box exists
		if not (self.checkBoxExists(boxName) or self.checkArchivedBoxExists(boxName)):
			print('box {} doesn\'t exist'.format(boxName))
			return
		#ask user to confirm the operation
		print('Are you sure to delete box {} ?'.format(boxName))
		print('Note: All files will be lost (y/n)')
		answer=input()
		if answer == 'y':
			if self.checkBoxExits(boxName):
				shutil.removetree(self.getFullBoxPath(boxName))
			else:
				os.remove(getFullArchivedBoxPath(boxName))
		else:
			print('operation cancelled')
