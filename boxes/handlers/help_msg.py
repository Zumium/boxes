from boxes import handlerBase

class HelpHandler(handlerBase.BaseHandler):

	def __init__(self):
		super().__init__()

	def handle(self):
		helpMessage='''
usage: boxes COMMAND [OPTIONAL ARGUMENTS]

boxes create BOX_NAME	--	create a new box named BOX_NAME
boxes drop BOX_NAME	--	delete the box named BOX_NAME
boxes list-boxes	--	list all unpacked boxes
boxes list-arch		--	list all packed boxes
boxes list-file BOX_NAME	--	list all files in the box named BOX_NAME
boxes list		--	list all of both packed and unpacked boxes
boxes link BOX_NAME[:FILE_NAME] [PATH]	--	link BOX_NAME[:FILE_NAME] to the given path.Current working directory is as default
boxes unlink BOX_NAME[:FILE_NAME]	--	delete all links of BOX_NAME[:FILE_NAME]
boxes archive BOX_NAME	--	pack the box named BOX_NAME
boxes unarchive BOX_NAME	--	unpack the box named BOX_NAME
boxes path BOX_NAME	--	print out the path of box named BOX_NAME
boxes import BOX_ARCHIVE_FILE_PATH	--	import from an outer file into a packed box
boxes export BOX_NAME [PATH]	--	export a box to an outer file at given directory.Current working directory is as default
boxes add BOX_NAME FILE_NAME	--	copy given file into the given box
boxes del BOX_NAME:FILE_NAME	--	delete the given file that is in the box
boxes fresh [BOX_NAME[:FILE_NAME]] --	check links and delete those that are missing in record
'''
		print(helpMessage)
