from boxes import handlerBase

class FreshHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		#select mode
		mode=None
		if self.argumentNum == 0:
			#fresh all boxes and all files
			mode='all'
		#check number of arguments
		if self.argumentNum >= 2:
			print('usage: boxes fresh [BOX[:FILE]]')
			return
		#check type
		if self.argumentNum != 0:
			if self.arguments[0]['type'] != 'box' and self.arguments[0]['type'] != 'boxfile':
				print('usage: boxes fresh [BOX[:FILE]]')
				return
		#select mode
		if self.arguments[0]['type'] == 'box':
			mode='box'
		else:
			mode='boxfile'
		#call corresponding function
		if mode == 'all':
			self.freshall()
		else mode == 'box':
			self.freshbox(self.arguments[0]['box'])
		else mode == 'boxfile':
			self.freshfile(self.arguments[0]['box'],self.arguments[0]['file'])

	def freshfile(self,boxName,fileName):
		import os.path
		links=self.getLinkList(boxName,fileName)
		newLinks=list(filter(os.path.exists,links))
		self.writeLinkList(newLinks,boxName,fileName)

	def freshbox(self,boxName):
		import os
		import os.path
		#get list of file
		fileList=os.listdir(self.getFullBoxPath(boxName))
		fileList.remove('.box')
		#unlink box
		boxLinks=self.getLinkList(boxName)
		newBoxLinks=list(filter(os.path.exists),boxLinks)
		self.writeLinkList(newBoxLinks,boxName)
		#unlink file in the box:
		for eachFile in fileList:
			self.freshfile(boxName,eachFile)

	def freshall():
		import os
		#get list of boxes
		boxList=os.listdir(self.getFullBoxPath(''))
		#fresh each box
		for eachBox in boxList:
			self.freshbox(eachBox)
