import nuke

def main():
	matchmove = nuke.selectedNode()
	nuke.selectAll()
	nuke.invertSelection()

	roto = nuke.createNode('Roto')
	roto['translate'].setExpression(f'{matchmove.name()}.translate')
	roto['rotate'].setExpression(f'{matchmove.name()}.rotate')
	roto['scale'].setExpression(f'{matchmove.name()}.scale')
	roto['center'].setExpression(f'{matchmove.name()}.center')
