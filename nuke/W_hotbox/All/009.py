#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Un / Premult
#
#----------------------------------------------------------------------------------------------------------

def emptySelection():
    for i in nuke.selectedNodes():
        i.knob('selected').setValue(False)
        
for i in nuke.selectedNodes():
    emptySelection()
    i.knob('selected').setValue(True)
    unPremultNode = nuke.createNode('Unpremult')
    premultNode = nuke.createNode('Premult')
    premultNode.knob('channels').setValue('rgb')
    
emptySelection()