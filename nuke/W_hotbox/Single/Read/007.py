#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: AOV Contact Sheets
#
#----------------------------------------------------------------------------------------------------------

import os, nuke, math


def main():
    try:
        n = nuke.selectedNode()
        if n.Class() == 'Read':
            path = os.path.dirname(n.knob('file').getValue())
            path = path.rsplit('/', 1)
            path = path[0]
            first_frame = int(n.knob('first').getValue())
            last_frame = int(n.knob('last').getValue())
    except:
        path = nuke.getFilename( 'Choose Sequence Parent Folder', '*/' )

    if not path:
        nuke.message('No path specified, exiting')
        return

    else:
        contactInputs = []

        for root, dirs, files in os.walk(path):
            for dir in dirs:
                # skip any hidden directories
                if dir[0] == '.':
                    continue

                dir = os.path.join(root, dir)
                nuke_files = nuke.getFileNameList(dir)
                # print files
                if not nuke_files:
                    print '%s directory is empty' % dir

                else:
                    for seq in nuke_files:
                        # print seq
                        if seq != '.thumbs' and seq != '':
                            currentNode = []
                            # print dir

                            # splits the file name from the frame range, starting at the right side
                            file_name, frame_range = seq.rsplit(' ', 1)

                            # create a path for the read nodes that is readable by nuke
                            readPath = os.path.join(dir, file_name)
                            # replaces backslashes with forward slashes (two backslashes because the backslash must be escaped)
                            readPath = readPath.replace("\\","/")
                            # print readPath

                            # create the read node and set its attributes
                            readNode = nuke.nodes.Read(file="%s" % (readPath))
                            readNode.knob('first').setValue(first_frame)
                            readNode.knob('last').setValue(last_frame)
                            readNode.knob('origfirst').setValue(first_frame)
                            readNode.knob('origlast').setValue(last_frame)

                            readNode.knob('on_error').setValue("checkerboard")

                            currentNode.append(readNode)

                            if 'Crypto' in file_name:
                                cryptoViewer = nuke.nodes.Cryptomatte()
                                cryptoViewer.setInput(0, currentNode[-1])
                                currentNode.append(cryptoViewer)


                            # create a text node with the name of the pass attached to the read node
                            textNode = nuke.nodes.Text2(global_font_scale = .3)
                            textNode.knob('box').setValue([0, 0, 1920, 50])
                            textNode.knob('message').setValue("%s" % (file_name))
                            textNode.knob('enable_background').setValue(True)
                            textNode.setInput(0, currentNode[-1])
                            currentNode.append(textNode)

                            frameTextNode = nuke.nodes.Text2(global_font_scale = .5)
                            frameTextNode.knob('box').setValue([1620, 0, 1910, 50])
                            frameTextNode.knob('xjustify').setValue('right')
                            frameTextNode.knob('message').setValue('[frame]')
                            frameTextNode.knob('color').setValue([1, 0, 0, 1])
                            frameTextNode.setInput(0, currentNode[-1])
                            currentNode.append(frameTextNode)

                            contactInputs.append(frameTextNode)

        if not contactInputs:
            nuke.message('something broke, maybe empty directories?')
        else:
            cSheet = nuke.nodes.ContactSheet(inputs = contactInputs)

            count = len(contactInputs)
            countSqrt = math.sqrt( count )
            rowsCols = math.ceil( countSqrt )

            cSheet.knob('rows').setValue(int(rowsCols))
            cSheet.knob('columns').setValue(int(rowsCols))
            cSheet.knob('width').setValue(int(rowsCols) * 1920)
            cSheet.knob('height').setValue(int(rowsCols) * 1080)

main()