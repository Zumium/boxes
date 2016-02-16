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

class ArchiveHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		import os.path
		import os
		import tarfile
		import subprocess
		import shutil
		#check numbers of argument
		if self.argumentNum != 1:
			print('usage: boxes archive BOX')
			return
		#check argument's type
		if self.arguments[0]['type'] != 'box':
			print('usage: boxes archive BOX')
			return
		#check whether it already exists as an archive
		boxName=self.arguments[0]['box']
		if self.checkArchivedBoxExists(boxName):
			print('box {} already exists as an archive'.format(boxName))
			return
		#check whether it exists
		if not self.checkBoxExists(boxName):
			print('box {} doesn\'t exist'.format(boxName))
			return
		#start to archive the box
		#first, back up the current working directory
		preCwd=os.path.abspath(os.getcwd())
		#then , change current working directory to boxes' parent foler path
		os.chdir(self.getFullBoxPath(''))
		#create archive file
		boxTarFile=tarfile.open(self.getFullArchivedBoxPath(boxName),'w:'+self.compressType)
		#unlink the box
		subprocess.call(['boxes','unlink',boxName])
		#add box to tarfile
		boxTarFile.add(boxName)
		#close tarfile
		boxTarFile.close()
		#change working directory back
		os.chdir(preCwd)
		#drop the box
		shutil.rmtree(self.getFullBoxPath(boxName))
