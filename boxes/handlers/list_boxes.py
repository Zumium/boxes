import os
import xml.etree.ElementTree as ET

def handle(storageXML,cmdXML):
	#get folder path and archive path
	folderPath=storageXML.find('folderPath').text
	#and / if it is missing 
	if folderPath[len(folderPath)-1] != '/':
		folderPath+='/'
	#get list of boxes
	boxes=os.listdir(folderPath)
	output=' '.join(boxes)
	print(output)
