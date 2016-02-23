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
import platform

def parseCmdline():
	#get command line arguments
	args=sys.argv
	#number of arguments
	numArgs=len(args)
	#seperate different part
	argsSepeGroup=list()
	#add action
	argsSepeGroup.append([args[1],'']) #leave second element blank for action arguments
	firstArgPos=None
	secondArsPos=None
	#查找参数的位置
	for index in range(2,numArgs):
		if args[index][0] != '-':
			if firstArgPos==None:
				firstArgPos=index
			elif secondArsPos==None:
				secondArsPos=index
			else:
				print('Too much arugments')
				exit()
	#截取参数并添加到参数组列表
	if firstArgPos != None:
		argsSepeGroup.append(args[2:firstArgPos+1])
	if secondArsPos != None:
		argsSepeGroup.append(args[firstArgPos+1:secondArsPos+1])
	#解析action的附带参数
	if args[-1][0]=='-':
		argsSepeGroup[0][1]=args[-1][1:]
	#反转和去短横线
	for index in range(1,len(argsSepeGroup)):
		if len(argsSepeGroup[index]) != 1:
			argsSepeGroup[index][0]=argsSepeGroup[index][0][1:]#去短横线
			argsSepeGroup[index].reverse()#翻转
	#生成解析树
	return getParseTree(argsSepeGroup)

def getParseTree(argsList):
	#根节点
	cmd=ET.Element('cmd')
	#action 节点
	action=ET.SubElement(cmd,'action')
	action.attrib['paranum']=str(len(argsList)-1)
	action.attrib['args']=argsList[0][1]
	#参数节点
	for index in range(1,len(argsList)):
		parameter=argsList[index]
		argNode=ET.SubElement(cmd,'para')
		argNode.attrib['index']=str(index-1)
		if len(parameter) == 1:
			#未指定类型，启用自动判断
			pathSeperator=None
			if platform.system() != 'Windows':
				#take other systems as unix
				pathSeperator='/'
			else:
				pathSeperator='\\'
			if parameter[0].find(':') < 0 :
				#box or path
				if parameter[0].find(pathSeperator) >= 0 :
					#is path
					argNode.attrib['type']='path'
					path=ET.SubElement(argNode,'path')
					path.text=parameter[0]
				else:
					#is box name
					argNode.attrib['type']='box'
					box=ET.SubElement(argNode,'box')
					box.text=parameter[0]
			else:
				#box_name:file_name
				argNode.attrib['type']='boxfile'
				paramSplit=parameter[0].split(':')
				boxName=ET.SubElement(argNode,'box')
				boxName.text=paramSplit[0]
				fileName=ET.SubElement(argNode,'file')
				fileName.text=paramSplit[1]
		else:
			#指定了类型
			if parameter[1] == 'p':
				#指定为path类型
				argNode.attrib['type']='path'
				path=ET.SubElement(argNode,'path')
				path.text=parameter[0]
			elif parameter[1] == 'b':
				#指定为box类型
				argNode.attrib['type']='box'
				box=ET.SubElement(argNode,'box')
				box.text=parameter[0]
			elif parameter[1] == 'f':
				#指定为box:file类型
				argNode.attrib['type']='boxfile'
				boxNode=ET.SubElement(argNode,'box')
				fileNode=ET.SubElement(argNode,'file')
				boxFileSepeList=parameter[0].split(':')
				boxNode.text=boxFileSepeList[0]
				fileNode.text=boxFileSepeList[1]
	return cmd
