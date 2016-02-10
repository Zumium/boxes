import os.path
import shutil
import xml.etree.ElementTree as ET

def handle(storageXML,cmdXML):
	#get folder path
	folderPath=storageXML.find('folderPath').text
	if folderPath[len(folderPath)-1] != '/':
		folderPath+='/'
	#check parameters
	#check number of parameters
	if cmdXML.find('action').attrib['paranum'] != '2':
		print('ADD command should be followed by 2 parameters')
		exit()
	#check parameters' type
	for x in cmdXML.findall('para'):
		if x.attrib['index'] == '0' and x.attrib['type'] != 'box':
			print('first argument should be a box name')
			exit()
		elif x.attrib['index'] == '1' and x.attrib['type'] != 'path':
			print('second argument should be a path refer to the file you wanna add')
			exit()
	#check if box exists
	boxName=None
	srcPath=None
	for x in cmdXML.findall('para'):
		if x.attrib['index'] == '0':
			boxName=x.find('box').text
		else:
			srcPath=x.find('path').text
	boxPath=folderPath+boxName
	if not os.path.isdir(boxPath):
		print('box {} doesn\'t exist'.format(boxName))
		exit()
	#check if the file exists
	if not os.path.exists(srcPath):
		print('file {} doesn\'t exist'.format(srcPath))
		exit()
	if os.path.isfile(srcPath):
		#copy file to box folder
		shutil.copy(srcPath,boxPath)
	elif os.path.isdir(srcPath):
		#copy whole directory into box folder
		shutil.copytree(srcPath,boxPath)
	else:
		print('cannot add the specified file into the box')
