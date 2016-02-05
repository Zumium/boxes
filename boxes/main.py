#! /usr/bin/env python3

from boxes import argsParse,configParse
from boxes.handlers import *

import xml.etree.ElementTree as ET
import configparser

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
	ET.SubElement(storage,'folderPath').text=folderPath
	ET.SubElement(storage,'archivePath').text=archivePath
	
	#
	operaHandlers={'create':create.handle,'drop':drop.handle}
	cmdAction=xmlCmdArgs.find('action').text
	operaHandlers[cmdAction](storage,xmlCmdArgs)
	
	
