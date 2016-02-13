from boxes import handlerBase

class ListArchivesHandler(handlerBase.BaseHandler):
	
	def __init__(self):
		super().__init__()

	def handle(self):
		import os
		#get list of boxes
		boxes_list=os.listdir(self.archivePath)
		#drop .tar.gz tail
		boxes_name=list(map(lambda x:x[:x.find(self.archiveTail)],boxes_list))
		#print it out
		output='   '.join(boxes_name)
		print(output)
