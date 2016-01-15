import sys
import xml.etree.ElementTree as ET

def parseCmdline():
	#get number of parameters
	args=sys.argv
	paramNum=len(args)
	#build root element
	cmd=ET.Element('cmd')
	#build "action" element
	action=ET.SubElement(cmd,'action')
	action.attrib['paranum']=str(paramNum-2)
	action.text=args[1]
	#if action is set,then parse in a different way
	if args[1] == 'set' :
		setting_types=['setting_key','setting_value']
		for index in list(range(2,paramNum)) :
			para=ET.SubElement(cmd,'para')
			para.attrib['index']=str(index-2)
			para.attrib['type']=setting_types[index-2]
			para.text=args[index]
			
	else:
		#parse last two parameters
		for index in list(range(2,paramNum)) :
			param=args[index]
			para=ET.SubElement(cmd,'para')
			para.attrib['index']=str(index-2)
			if param.find(':') < 0 :
				#box or path
				if param.find('/') >= 0 :
					#is path
					para.attrib['type']='path'
					path=ET.SubElement(para,'path')
					path.text=param
				else:
					#is box name
					para.attrib['type']='box'
					box=ET.SubElement(para,'box')
					box.text=param
			else:
				#box_name:file_name
				para.attrib['type']='boxfile'
				paramSplit=param.split(':')
				boxName=ET.SubElement(para,'box')
				boxName.text=paramSplit[0]
				fileName=ET.SubElement(para,'file')
				fileName.text=paramSplit[1]
	
	return cmd 
