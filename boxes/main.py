#! /usr/bin/env python3
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

from boxes import argsParse,configParse
from boxes.handlers import *

import xml.etree.ElementTree as ET
import configparser
import os.path

def main():
	#get command line arguments in xml tree format
	xmlCmdArgs=argsParse.parseCmdline()
	#get configfile
	configPath=configParse.getConfigPath()
	config=configParse.readConfig(configPath)
	#get folders and archives path and pack them into xml
	folderPath=config['Default']['FolderPath']
	archivePath=config['Default']['ArchivePath']
	#storage=ET.Element('storage')
	#ET.SubElement(storage,'folderPath').text=os.path.expanduser(folderPath) #Notice: in case that the user uses '~' symbol
	#ET.SubElement(storage,'archivePath').text=os.path.expanduser(archivePath)
	
	#
	#operaHandlers={'create':create.handle,'drop':drop.handle,'list-boxes':list_boxes.handle,'list-arch':list_archives.handle,'list':list_boxfile.handle,'add':add_file.handle}
	operaHandlers={'create':create.CreateHandler,'drop':drop.DropHandler,'list-file':list_boxfile.ListBoxfileHandler,'list-boxes':list_boxes.ListBoxesHandler,'list-arch':list_archives.ListArchivesHandler,'add':add_file.AddFileHandler,'path':path.PathHandler,'del':del_file.DelFileHandler,'link':link.LinkHandler,'unlink':unlink.UnlinkHandler,'fresh':fresh.FreshHandler,'archive':archive.ArchiveHandler,'unarchive':unarchive.UnarchiveHandler,'import':import_box.ImportHandler,'export':export_box.ExportHandler,'list':list_allboxes.ListHandler,'help':help_msg.HelpHandler}
	cmdAction=xmlCmdArgs.find('action').text
	handlerInstance=operaHandlers[cmdAction]()
	handlerInstance.setBoxPath(folderPath,archivePath)
	handlerInstance.putArgument(xmlCmdArgs)
	handlerInstance.handle()
