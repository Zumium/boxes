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

class ListBoxfileHandler(handlerBase.BaseHandler):
	
	def __init__(self):
		super().__init__()

	def handle(self):
		import os
		#check number of arguments
		if self.argumentNum != 1:
			print('LIST command can be followed with only one argument')
			return
		#check argument type
		if self.arguments[0]['type'] != 'box':
			print('LIST command can only be followed with box name')
			return
		#check if the box exists
		boxName=self.arguments[0]['box']
		if not self.checkBoxExists(boxName):
			print('box {} doesn\'t exist'.format(boxName))
			return
		#get file list
		file_list=os.listdir(self.getFullBoxPath(boxName))
		#do not display .box folder
		file_list.remove('.box')
		#print it out
		output='   '.join(file_list)
		print(output)
