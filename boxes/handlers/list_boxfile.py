import os
import os.path
import xml.etree.ElementTree as ET

def handle(storageXML,cmdXML):
	#get folder path
	folderPath=storageXML.find('folderPath').text
	if folderPath[len(folderPath)-1] != '/':
		folderPath+='/'
	#check parameters
	if cmdXML.find('action').attrib['paranum'] != '1':
		print('LIST command should be followed with only one BOX NAME')
		exit()
	if cmdXML.find('para').attrib['type'] != 'box':
		print('LIST command should be followed by BOX NAME')
		exit()
	#get list of files in the box
	boxName=cmdXML.find('para').find('box').text
	boxFolderPath=folderPath+boxName
	if not os.path.isdir(boxFolderPath):
		print('The box {} doesn\'t exist'.format(boxName))
		exit()
	file_list=os.listdir(boxFolderPath)
	file_list.remove('.box')
	output='  '.join(file_list)
	print(output)
	exit()
