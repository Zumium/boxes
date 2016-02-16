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
	#default action is help
	action.text='help'
	#get action
	if paramNum != 1:
		action.text=args[1]
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
