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

class UnarchiveHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os
		import os.path
		import tarfile
		import subprocess
		#check number of arguments
		if self.argumentNum != 1:
			print('usage: boxes unarchive BOX')
			return
		#check arugment's type
		if self.arguments[0]['type'] != 'box':
			print('usage: boxes unarchive BOX')
			return
		#check if archive exists
		archivedBoxName=self.arguments[0]['box']
		if not self.checkArchivedBoxExists(archivedBoxName):
			print('archived box {} doesn\'t exist'.format(archivedBoxName))
			return
		#start to unarchive
		#open tarfile
		boxTarFile=tarfile.open(self.getFullArchivedBoxPath(archivedBoxName),'r:'+self.compressType)
		#unarchive box
		boxTarFile.extractall(self.getFullBoxPath(''))
		#close tarfile
		boxTarFile.close()
		#remove archive file
		os.remove(self.getFullArchivedBoxPath(archivedBoxName))
		#fresh it up
		subprocess.call(['boxes','fresh','-b',archivedBoxName])
