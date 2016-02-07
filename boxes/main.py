#! /usr/bin/env python3

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
	storage=ET.Element('storage')
	ET.SubElement(storage,'folderPath').text=os.path.expanduser(folderPath) #Notice: in case that the user uses '~' symbol
	ET.SubElement(storage,'archivePath').text=os.path.expanduser(archivePath)
	
	#
	operaHandlers={'create':create.handle,'drop':drop.handle,'list-boxes':list_boxes.handle,'list-arch':list_archives}
	cmdAction=xmlCmdArgs.find('action').text
	operaHandlers[cmdAction](storage,xmlCmdArgs)
	
	
