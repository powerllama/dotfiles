#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Stencil
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    m = nuke.createNode('Merge2')
    m.knob('operation').setValue('stencil')