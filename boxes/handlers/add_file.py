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

class AddFileHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os.path
		import shutil
		#check arguments' number
		if self.argumentNum != 2:
			print('ADD command should be followed with 2 arguments')
			return
		#check argument type
		if self.arguments[0]['type'] != 'box' or self.arguments[1]['type'] != 'path':
			print('usage: boxes add BOX_NAME /path/to/file')
			return
		#check if box exists
		if not self.checkBoxExists(self.arguments[0]['box']):
			print('box {} doesn\'t exist'.format(self.arguments[0]['box']))
			return
		#check if path exists
		if not os.path.exists(self.arguments[1]['path']):
			print('{} doesn\'t exist'.format(self.arguments[1]['path']))
			return
		#figure out path is file or directory
		isDir=os.path.isdir(self.arguments[1]['path'])
		if isDir:
			#is a directory
			#get directory's name
			dirName=None
			dirPath=self.arguments[1]['path']
			pathSplit=dirPath.split(self.pathSeperator)
			if pathSplit[-1] == '':
				dirName=pathSplit[-2]
			else:
				dirName=pathSplit[-1]
			newDirPath=self.getFullBoxPath(self.arguments[0]['box'],withSlash=True)+dirName
			shutil.copytree(dirPath,newDirPath)
		else:
			#is a file
			shutil.copy(self.arguments[1]['path'],self.getFullBoxPath(self.arguments[0]['box']))
