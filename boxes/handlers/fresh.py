#Copyright (C) 2016 Zumium martin007323@gmail.com
#
#
#Licensed to the Apache Software Foundation (ASF) under one
#or more contributor license agreements.  See the NOTICE file
#distributed with this work for additional information
#regarding copyright ownership.  The ASF licenses this file
#to you under the Apache License, Version 2.0 (the
#"License"); you may not use this file except in compliance
#with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an
#"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#KIND, either express or implied.  See the License for the
#specific language governing permissions and limitations
#under the License.
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
		else:
			#check number of arguments
			if self.argumentNum >= 2:
				print('usage: boxes fresh [BOX[:FILE]]')
				return
			#check type
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
		elif mode == 'box':
			self.freshbox(self.arguments[0]['box'])
		elif mode == 'boxfile':
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
		newBoxLinks=list(filter(os.path.exists,boxLinks))
		self.writeLinkList(newBoxLinks,boxName)
		#unlink file in the box:
		for eachFile in fileList:
			self.freshfile(boxName,eachFile)

	def freshall(self):
		import os
		import os.path
		#get list of boxes
		boxList=os.listdir(self.getFullBoxPath(''))
		#remove all non-directory things
		boxList=list(filter(lambda x:os.path.isdir(x),boxList))
		#remove hidden folders
		boxList=list(filter(lambda x:x[0]!='.',boxList))
		#fresh each box
		for eachBox in boxList:
			self.freshbox(eachBox)
