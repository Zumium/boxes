from boxes import handlerBase

class PathHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		#check number of arguments
		if self.argumentNum != 1:
			print('PATH command should be followed with only 1 argument')
			return
		#check type of argument
		if self.arguments[0]['type'] != 'box':
			print('PATH command can only be followed with box name')
			return
		#print it out
		print(self.getFullBoxPath(self.arguments[0]['box'],withSlash=True))
