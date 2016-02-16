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

class LinkHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os
		import os.path
		#check number of arguments
		if self.argumentNum == 0:
			print('LINK command need at least 1 argument')
			return
		if self.argumentNum == 1:
			#path is not set,use current working directory sas default
			cwdPath=os.getcwd()
			if cwdPath[-1] != self.pathSeperator:
				cwdPath+=self.pathSeperator
			self.arguments.append({'path':cwdPath,'type':'path'})
		#check type
		if (self.arguments[0]['type'] != 'box' and self.arguments[0]['type'] != 'boxfile') or self.arguments[1]['type'] != 'path':
			print('usage: box link BOX[:FILE] /path/to/link')
			return
		#get link type
		isBox=None
		if self.arguments[0]['type'] == 'box':
			isBox=True
		else:
			isBox=False
		#check if exists
		if isBox:
			if not self.checkBoxExists(self.arguments[0]['box']):
				print('box {} doesn\'t exist'.format(self.arguments[0]['box']))
				return
		else:
			if not self.checkFileExists(self.arguments[0]['box'],self.arguments[0]['file']):
				print('file {0} in box {1} doesn\'t exist'.format(self.arguments[0]['file'],self.arguments[0]['box']))
				return
		#get link file name
		boxName=None
		fileName=None
		linkFilePath=None
		linkFileParentPath=os.path.abspath(self.arguments[1]['path'])
		if linkFileParentPath[-1] != self.pathSeperator:
			linkFileParentPath+=self.pathSeperator

		if isBox:
			boxName=self.arguments[0]['box']
			linkFilePath=linkFileParentPath+boxName
			os.symlink(self.getFullBoxPath(boxName),linkFilePath)
		else:
			boxName=self.arguments[0]['box']
			fileName=self.arguments[0]['file']
			linkFilePath=linkFileParentPath+fileName
			os.symlink(self.getFilePath(boxName,fileName),linkFilePath)
		#add link path to record file
		self.addLink(linkFilePath,boxName,fileName)
