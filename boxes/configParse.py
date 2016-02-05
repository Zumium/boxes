import configparser
import os
import os.path

def getConfigPath():
	configPath=[os.path.expanduser('~/.boxesrc'),'/usr/local/etc/boxes/boxesrc','/etc/boxes/boxesrc']
	config=None
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

def saveConfig(config,configPath):
	configfile=open(configPath,'w')
	config.write(configfile)
	configfile.close()
