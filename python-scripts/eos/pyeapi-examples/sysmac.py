#!/usr/bin/env python
from __future__ import print_function
import pyeapi

pyeapi.load_config('nodes.conf')
node = pyeapi.connect_to('leaf4')

output = node.enable('show version')

print(('Leaf4 System MAC address is', output[0]['result']['systemMacAddress']))
print(output)
