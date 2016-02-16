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

class UnlinkHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import subprocess
		import os
		#check number of arguments
		if self.argumentNum != 1:
			print('usage: boxes unlink BOX[:FILE]')
			return
		#check type
		if self.arguments[0]['type'] != 'box' and self.arguments[0]['type'] != 'boxfile':
			print('usage: boxes unlink BOX[:FILE]')
			return
		#is user asking to unlink box or a file in box
		isBox=(self.arguments[0]['type'] == 'box')
		boxName=None
		fileName=None
		#read arguments
		if isBox:
			boxName=self.arguments[0]['box']
		else:
			boxName=self.arguments[0]['box']
			fileName=self.arguments[0]['file']
		#check if it exists
		if isBox:
			if not self.checkBoxExists(boxName):
				print('box {} doesn\'t exist'.format(boxName))
				return
		else:
			if not self.checkFileExists(boxName,fileName):
				print('file {0} in box {1} doesn\'t exist'.format(fileName,boxName))
				return
		if isBox:
			#fresh it first
			subprocess.call(['boxes','fresh',boxName])
			#get file list in the box
			fileList=os.listdir(self.getFullBoxPath(boxName))
			fileList.remove('.box')
			#unlink box
			boxLinks=self.getLinkList(boxName)
			for each in boxLinks:
				os.unlink(each)
			self.writeLinkList([],boxName)
			#unlink each file
			for eachFile in fileList:
				links=self.getLinkList(boxName,eachFile)
				for each in links:
					os.unlink(each)
				self.writeLinkList([],boxName,eachFile)
		else:
			#fresh it first
			subprocess.call(['boxes','fresh',boxName+':'+fileName])
			#unlinking
			links=self.getLinkList(boxName,fileName)
			for each in links:
				os.unlink(each)
			self.writeLinkList([],boxName,fileName)
