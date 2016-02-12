from boxes import handlerBase

class ListBoxesHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os
		#get list of boxes
		boxes_list=os.listdir(self.getFullBoxPath(''))
		#print it out
		output='   '.join(boxes_list)
		print(output)
