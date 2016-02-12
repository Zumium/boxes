from boxes import handlerBase

class ListBoxfileHandler(handlerBase.BaseHandler):
	
	def __init__(self):
		super().__init__()

	def handle(self):
		import os
		#check number of arguments
		if self.argumentNum != 1:
			print('LIST command can be followed with only one argument')
			return
		#check argument type
		if self.arguments[0]['type'] != 'box':
			print('LIST command can only be followed with box name')
			return
		#check if the box exists
		boxName=self.arguments[0]['box']
		if not self.checkBoxExists(boxName):
			print('box {} doesn\'t exist'.format(boxName))
			return
		#get file list
		file_list=os.listdir(self.getFullBoxPath(boxName))
		#do not display .box folder
		file_list.remove('.box')
		#print it out
		output='   '.join(file_list)
		print(output)
