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

class HelpHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		helpMessage='''
Copyright (C) 2016 Zumium martin007323@gmail.com

usage: boxes COMMAND [OPTIONAL ARGUMENTS]

boxes create BOX_NAME	--	create a new box named BOX_NAME
boxes drop BOX_NAME	--	delete the box named BOX_NAME
boxes list-boxes	--	list all unpacked boxes
boxes list-arch		--	list all packed boxes
boxes list-file BOX_NAME	--	list all files in the box named BOX_NAME
boxes list		--	list all of both packed and unpacked boxes
boxes link BOX_NAME[:FILE_NAME] [PATH]	--	link BOX_NAME[:FILE_NAME] to the given path.Current working directory is as default
boxes unlink BOX_NAME[:FILE_NAME]	--	delete all links of BOX_NAME[:FILE_NAME]
boxes archive BOX_NAME	--	pack the box named BOX_NAME
boxes unarchive BOX_NAME	--	unpack the box named BOX_NAME
boxes path BOX_NAME	--	print out the path of box named BOX_NAME
boxes import BOX_ARCHIVE_FILE_PATH	--	import from an outer file into a packed box
boxes export BOX_NAME [PATH]	--	export a box to an outer file at given directory.Current working directory is as default
boxes add BOX_NAME FILE_NAME	--	copy given file into the given box
boxes del BOX_NAME:FILE_NAME	--	delete the given file that is in the box
boxes fresh [BOX_NAME[:FILE_NAME]] --	check links and delete those that are missing in record

This software is released under Apache License Version 2.0 (http://www.apache.org/licenses/)
'''
		print(helpMessage)
