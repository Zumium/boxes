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

class ImportHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import shutil
		import os.path
		#check number of arguments
		if self.argumentNum != 1:
			print('usage: boxes import BOX_ARCHIVE_FILE_PATH')
			return
		#check argument's type
		if self.arguments[0]['type'] != 'path':
			print('usage: boxes import BOX_ARCHIVE_FILE_PATH')
			return
		#check whether file exists
		importFilePath=os.path.abspath(self.arguments[0]['path'])
		if not os.path.isfile(importFilePath):
			print('{} is not a file'.format(importFilePath))
			return
		#copy tarfile to archived boxes' directory
		shutil.copy(importFilePath,self.archivePath)
