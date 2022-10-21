# list of folders
# list of contents of folder
# create read nodes using each file
# attach read nodes to contact sheet - skip first read node
# connect contact sheets to switch



import math, os, nuke

main()

def main():
	switchInputs = []
	path = nuke.getFilename( 'Choose Sequence Parent Folder', '*/' )

	if not path:
		nuke.message('No path specified, exiting')
		return

	else:
		for root, dirs, files in os.walk(path):
			dirs.sort()
			for dir in dirs:
				contactInputs = []

				# skip any hidden directories
				if dir[0] == '.':
					continue

				dir = os.path.join(root, dir)
				nuke_files = nuke.getFileNameList(dir)
				nuke_files.sort()

				if not nuke_files:
					print '%s directory is empty' % dir

				else:
					for seq in nuke_files:
						if seq != '.thumbs' and seq != '':
							# currentNode=[]

							# splits the file name from the frame range, starting at the right side
	                        file_name, frame_range = seq.rsplit(' ', 1)

	                        # grab the first and last frame
	                        firstFrame, lastFrame = frame_range.split('-')

	                        # get range between frames, I want individual read nodes, not sequences
	                        fileRange = range(int(firstFrame), int(lastFrame)+1)

	                        # skip first file in folder with [1:]
	                        for i in fileRange[1:]:
	                        	#create a path for the read nodes that is readable by nuke
	                        	readPath = os.path.join(dir, file_name)
	                        	# replaces backslashes with forward slashes
	                        	readPath = readPath.replace("\\", "/")

	                        	readNode = nuke.nodes.Read(file="%s" % (readPath))

	                        	readNode.knob('first').setValue(i)
	                        	readNode.knob('last').setValue(i)
	                            readNode.knob('origfirst').setValue(i)
	                            readNode.knob('origlast').setValue(i)

	                            contactInputs.append(readNode)


		        if not contactInputs:
		        	nuke.message('something broke, maybe empty directories?')

		        else:
		        	cSheet = nuke.nodes.ContactSheet(inputs = contactInputs)

		        	count = len(contactInputs)
		        	cSheet.knob('rows').setValue(count)
		        	cSheet.knob('columns').setValue(1)
		        	cSheet.knob('width').setValue(1920)
		        	cSheet.knob('height').setValue(count * 1080)

		        	switchInputs.append(cSheet)

	cSheetSwitch = nuke.nodes.Switch(inputs = switchInputs)