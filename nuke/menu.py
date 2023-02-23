##### menu.py is where you put customizations that you want to appear in the GUI #####

### import Python scripts and/or Python Modules
import nuke
import sys


# Tell nuke to look for the gizmos in these folders
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./python')
# nuke.pluginAddPath("./gizmos/WaveMachine_v1.0")


# Preview values of the amount of blur, defocus, time offset, tracker
nuke.knobDefault('Blur.label','size: [value size]')
nuke.knobDefault('Defocus.label','size: [value defocus]')
nuke.knobDefault('TimeOffset.label','[value time_offset]')
nuke.knobDefault('Tracker4.label', '[value transform]\n[value reference_frame]')

# Set default RotoPaint timeline to all frames
# Roto clip_type
nuke.knobDefault("Roto.clip_type", "none")
nuke.knobDefault("RotoPaint.clip_type", "none")

# Set defaults for ContactSheets
# Sets relevant expressions in relevant knobs to automagically figure out the contact sheet's resolution, rows, columns, etc.
nuke.knobDefault("ContactSheet.width", '{"input.width * columns"}')
nuke.knobDefault("ContactSheet.height", '{"input.height * rows"}')
nuke.knobDefault("ContactSheet.roworder", 'TopBottom')
nuke.knobDefault("ContactSheet.colorder", 'LeftRight')
nuke.knobDefault("ContactSheet.rows", '{"ceil(inputs/columns)"}')
nuke.knobDefault("ContactSheet.columns", '{"ceil(sqrt(inputs))"}')

# # We have to define a function, which will be used to add the resolution multiplier knob.
# def OnCScreation():

#     cs = nuke.thisNode()
#     k = nuke.Double_Knob('resMult', "Resolution Multiplier")
#     k.setRange(0.1,2)
#     k.setValue(1)

#     if cs != None:
#         cs.addKnob(k)

# # addOnCreate function says, "when I create a contact sheet node, run the OnCScreation fuction"
# nuke.addOnCreate(OnCScreation, nodeClass="ContactSheet")


# Create my nuke menus
toolbar = nuke.menu('Nodes')
abMenu = toolbar.addMenu('abTools')

abMenu.addCommand('Merge/Stencil','nuke.createNode("Merge2","operation stencil")', 'ctrl+alt+shift+s')
abMenu.addCommand('Merge/Mask','nuke.createNode("Merge2","operation mask")', 'ctrl+alt+shift+m')
# abMenu.addCommand('GradientEditor', 'nuke.createNode(\'h_gradienteditor\')', icon='h_gradienteditor.png')


# def addGroupTool(toolName):
#     g = nuke.nodePaste("Z:/.nuke/gizmos/" + toolName)
#     nuke.show(g)

abMenu.addCommand('fresnel', 'nuke.createNode(\"nFresnelMatte.gizmo")')
abMenu.addCommand('Utility/CurveConverter', 'nuke.createNode("CurveConverter.nk")' , icon='CurveConverter.png')
abMenu.addCommand('Grain_ARRI_Alexa', 'nuke.createNode("Grain_ARRI_Alexa.gizmo")')
abMenu.addCommand('reProject3D', 'nuke.createNode("ReProject3D.gizmo")')
abMenu.addCommand('transformmix', 'nuke.createNode("Transform_Mix.gizmo")')

# FrameHold modifications
def OnFrameHoldCreate():
    nFH = nuke.thisNode()
    if nFH != None:
        nFH['first_frame'].setValue(nuke.frame())

# Add the actions to newly created nodes
nuke.addOnUserCreate(OnFrameHoldCreate, nodeClass="FrameHold")


#Node Movements
def moveNodesUp():
    # Select all nodes above the currently selected node
    curYPos = nuke.selectedNode()['ypos'].getValue()
    for n in nuke.allNodes():
        if n['ypos'].getValue() < (curYPos - 40):
            n['ypos'].setValue(n['ypos'].getValue() - 40)

def moveNodesDown():
    # Select all nodes below the currently selected node
    curYPos = nuke.selectedNode()['ypos'].getValue()
    for n in nuke.allNodes():
        if n['ypos'].getValue() > (curYPos + 40):
            n['ypos'].setValue(n['ypos'].getValue() + 40)

def moveNodesLeft():
    # Select all nodes to the left of the currently selected node
    curXPos = nuke.selectedNode()['xpos'].getValue()
    for n in nuke.allNodes():
        if n['xpos'].getValue() < (curXPos - 80):
            n['xpos'].setValue(n['xpos'].getValue() - 80)

def moveNodesRight():
    # Select all nodes to the right of the currently selected node
    curXPos = nuke.selectedNode()['xpos'].getValue()
    for n in nuke.allNodes():
        if n['xpos'].getValue() > (curXPos + 80):
            n['xpos'].setValue(n['xpos'].getValue() + 80)

def mirrorNodes():
    # Mirror nodes horizontally or vertically
    nodes = nuke.selectedNodes()

    if len( nodes ) < 2:
        return False

    positions = [float(n.xpos() + n.screenWidth() * .5) for n in nodes ]
    axis = sum(positions) / len(positions)
    for n in nodes:
        n.setXpos(int( n.xpos() - 2*(n.xpos() + n.screenWidth()*.5 - axis)))

abMenu.addCommand('Utility/Mirror Nodes','mirrorNodes()','ctrl+shift+m')
abMenu.addCommand('Utility/Move Up','moveNodesUp()','ctrl+alt+up')
abMenu.addCommand('Utility/Move Down','moveNodesDown()','ctrl+alt+down')
abMenu.addCommand('Utility/Move Left','moveNodesLeft()','ctrl+alt+left')
abMenu.addCommand('Utility/Move Right','moveNodesRight()','ctrl+alt+right')



# Add python
# BackdropPro
import labelAutobackdrop
abMenu.addCommand('Shortcut/Auto Backdrop', 'labelAutobackdrop.autoBackdrop()', 'Shift+b')

import contactSheets
abMenu.addCommand('Utility/AOV Contact Sheet', 'contactSheets.main()')


import splitLayers
abMenu.addCommand('Utility/splitLayers', 'splitLayers.main()')

# W_ScaleTree
import W_scaleTree
abMenu.addCommand('Utility/Node/W_scaleTree', 'W_scaleTree.scaleTreeFloatingPanel()', 'alt+`')

# W_hotbox
import W_hotbox, W_hotboxManager

# KnobScripter
import KnobScripter

# channel_hotbox
import channel_hotbox
abMenu.addCommand('Channel HotBox', 'channel_hotbox.start()', 'alt+q')

# firefly killer
abMenu.addCommand('Firefly Killer', 'addGroupTool("FireflyKiller.gizmo")')

import NukeServerSocket
