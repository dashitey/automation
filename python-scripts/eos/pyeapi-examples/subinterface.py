import pyeapi

node = pyeapi.connect_to('veos01')

node.api('ipinterfaces').create('Ethernet1')

node.api('interfaces').create('Ethernet1.1')

node.api('interfaces').set_encapsulation('Ethernet1.1', 4)
