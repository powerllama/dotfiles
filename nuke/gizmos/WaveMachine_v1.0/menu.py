import os
import nuke

baseDir = os.path.dirname(__file__).replace("\\", "/")
nodesDir = os.path.join(baseDir, "nodes").replace("\\", "/")

toolbar = nuke.menu("Nodes")
toolbar.removeItem("Wave Machine")
wmMenu = toolbar.addMenu("Wave Machine", icon="waveMachine.png")
def buildMenu(parentMenu, dirPath):
    for fileName in os.listdir(dirPath):
        filePath = os.path.join(dirPath, fileName).replace("\\", "/")
        if os.path.isdir(filePath):
            subMenu = parentMenu.addMenu(fileName)
            buildMenu(subMenu, filePath)
        else:
            nodeBaseName = os.path.splitext(fileName)[0].split("_")[0]
            iconFileName = "{}.png".format(nodeBaseName)
            parentMenu.addCommand(nodeBaseName, "nuke.nodePaste('{}')".format(filePath), icon=iconFileName)

buildMenu(wmMenu, nodesDir)
