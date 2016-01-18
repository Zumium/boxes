import os
import xml.etree.ElementTree as ET

def createHandler(folderPath,archivePath,cmdXML):
	#check number of parameters
	actionElem=cmdXML.find('action')
	if actionElem.attrib['paranum'] != '1':
		print('CREATE command should be followed with only one argument')
		exit()
	#check parameter type
	paraElem=cmdXML.find('para')
	paraElem.attrib['type'] != 'box':
		print('CREATE command can be followed only with box name')
		exit()
	#create box folder under folderPath
	boxName=paraElem.find('box').text
	boxFolderFullPath=folderPath+boxName
	#check if the box already exists
	if os.path.isdir(boxFolderFullPath):
		print('box already exists')
		exit()
	elif os.path.isfile(archivePath+boxName+'.tar.gz'):
		print('box exists as an archivement')
		exit()
	os.mkdir(boxFolderFullPath)
	#create hidden folder for storaging links
	hiddenLinkFolderName='.box'
	os.mkdir(boxFolderFullPath+hiddenLinkFolderName)
	
