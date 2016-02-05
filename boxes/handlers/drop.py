import os
import xml.etree.ElementTree as ET
import shutil

def handle(storageXML,cmdXML):
	#get folderpath and archivepath
	folderPath=storageXML.find('folderPath').text
	archivePath=storageXML.find('archivePath').text
	#check number of parameters
	actionElem=cmdXML.find('action')
	if actionElem.attrib['paranum'] != '1':
		print('DROP command should be followed with only one argument')
		exit()
	#check parameter type
	paraElem=cmdXML.find('para')
	paraElem.attrib['type'] != 'box':
		print('DROP command can be followed only with box name')
		exit()
	#create box folder under folderPath
	boxName=paraElem.find('box').text
	boxFolderFullPath=folderPath+boxName
	#check if the box exists
	boxPath={'isfolder':False,'path':''}
	if os.path.isdir(boxFolderFullPath):
		boxPath['isfolder']=True
		boxPath['path']=boxFolderFullPath
	elif os.path.isfile(archivePath+boxName+'.tar.gz'):
		boxPath['isfolder']=False
		boxPath['path']=archivePath+boxName+'.tar.gz'
	else:
		print("the box required doesn't exist")
		exit()
	#double check 
		print('Are you going to delete box:{}(y/N)'.format(boxName))
		answer=input()
		if answer=='y':
			if boxPath['isfolder']:
				shutil.rmtree(boxPath['path'])
			else:
				os.remove(boxPath['path'])
	
