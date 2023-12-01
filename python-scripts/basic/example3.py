#=====================================================
# Example-3: Reading JSON file converting to text file 
#=====================================================
# Input file: 
#      device.json

# Output file
# Text filename: device.text


import json

with open('device.json', 'r') as y:
        datafile = json.load(y)


with open('device.text', 'w') as d:
        print(datafile, file=d)

