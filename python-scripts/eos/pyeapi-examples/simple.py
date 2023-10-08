#!/usr/bin/env python
from __future__ import print_function
import pyeapi
pyeapi.load_config('nodes.conf')
connection = pyeapi.connect(host = '192.168.0.21')
output = connection.execute(['enable', 'show version'])

print(('My system MAC address is', output['result'][1]['systemMacAddress']))


