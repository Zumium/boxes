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

class DropHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import shutil
		import os
		import subprocess
		#check number of arguments
		if self.argumentNum != 1:
			print('DROP command should be followed with only one argument')
			return
		#check argument type
		if self.arguments[0]['type'] != 'box':
			print('DROP command can be only followed by box name')
			return
		#get box name
		boxName=self.arguments[0]['box']
		#check if the box exists
		if not (self.checkBoxExists(boxName) or self.checkArchivedBoxExists(boxName)):
			print('box {} doesn\'t exist'.format(boxName))
			return
		#ask user to confirm the operation
		print('Are you sure to delete box {} ?'.format(boxName))
		print('Note: All files will be lost (y/n)')
		answer=input()
		if answer == 'y':
			if self.checkBoxExists(boxName):
				subprocess.call(['boxes','unlink',boxName])
				shutil.rmtree(self.getFullBoxPath(boxName))
			else:
				os.remove(self.getFullArchivedBoxPath(boxName))
		else:
			print('operation cancelled')
