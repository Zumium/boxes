from boxes import handlerBase

class ListHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import subprocess
		#check number of arguments
		if self.argumentNum != 0:
			print('usage: boxes list')
			return
		#list unarchived boxes
		print('Boxes:')
		print('')
		subprocess.call(['boxes','list-boxes'])
		#list archived boxes
		print('')
		print('Archives:')
		print('')
		subprocess.call(['boxes','list-arch'])
