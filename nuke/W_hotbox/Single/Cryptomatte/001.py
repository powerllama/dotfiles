#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Mask
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    m = nuke.createNode('Merge2')
    m.knob('operation').setValue('mask')
    #m.knob('Input').setValue(i)