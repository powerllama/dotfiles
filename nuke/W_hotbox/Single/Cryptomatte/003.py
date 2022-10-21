#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Grade
# COLOR: #7aa9ff
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

def emptySelection():
    for i in nuke.selectedNodes():
        i.knob('selected').setValue(False)
        
for i in nuke.selectedNodes():
    emptySelection()
    position = [i.xpos()-i.screenWidth()/2,i.ypos()+i.screenHeight()/2]
    g = nuke.createNode('Grade')
    g.setXpos(position[0]+210-g.screenWidth()/2)
    g.setYpos(position[1]-g.screenHeight()/2)
    g.setInput(1,i)