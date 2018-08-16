# change directonary
def CtoD():
    for node in nuke.selectedNodes():
        if node.Class() == 'Read':
            nsplit = node['file'].value().split('/') 
            if nsplit[0] == 'E:':
                nsplit[0] = 'D:'  
            elif nsplit[0] == 'D:':
                nsplit[0] = 'E:'
            njoin = '/'.join(nsplit)
            node['file'].setValue(njoin)
CtoD()



p = nuke.Panel('switch drive')
p.addButton('change to C:')
p.addButton('change to D:')

p.show()
