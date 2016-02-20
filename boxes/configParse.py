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
import configparser
import os
import os.path
import platform

def getConfigPath():
	config=None
	if platform.system() == 'Windows':
		#on windows system
		config=os.path.expanduser('~\\.boxesrc')
		if not os.path.isfile(config):
			config=None
	else:
		#on unix system
		configPath=[os.path.expanduser('~/.boxesrc'),'/usr/local/etc/boxes/boxesrc','/etc/boxes/boxesrc']
		for confPath in configPath:
			if os.path.isfile(confPath):
				config=confPath
				break

	if config==None:
		print('config file not found')
		exit()

	return config

def readConfig(configPath):
	config=configparser.ConfigParser()
	config.read(configPath)
	return config

#def saveConfig(config,configPath):
#	configfile=open(configPath,'w')
#	config.write(configfile)
#	configfile.close()
