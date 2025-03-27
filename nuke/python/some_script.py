''' This is to print all of the selected Read nodes '''
nodes = nuke.selectedNodes('Read')

for node in nodes:
    print(node['name'])