#================================================
# Example-1: Reading text file converting to JSON 
#================================================
# Input file: 
#      file1.text

# Output file
# Json filename: file1.json


import json

with open('file1', 'r') as f:
       datafile = (f.read()) 

with open('file1.json', 'w') as outfile:
    json.dump(datafile, outfile)