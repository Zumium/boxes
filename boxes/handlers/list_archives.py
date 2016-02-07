import os
import xml.etree.ElementTree as ET

def handle(storageXML,cmdXML):
	#get folder path and archive path
	archivePath=storageXML.find('archivePath').text
	#and / if it is missing 
	if archivePath[len(archivePath)-1] != '/':
		archivePath+='/'
	#get list of boxes
	boxes=os.listdir(archivePath)
	#get rid of .tar.gz tail
	archive_boxes=list(map(lambda x:x[:x.find('.tar.gz')],boxes))
	#print out the result
	output=' '.join(archive_boxes)
	print(output)
