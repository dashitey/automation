#================================================
# Example-2: Reading text file converting to YAML 
#================================================
# Input file: 
#      file2.text

# Output file
# Yaml filename: file2.yml


import yaml

with open('file2', 'r') as s:
        datafile = yaml.safe_load(s) 


with open('file2.yml', 'w') as outfile:
    yaml.dump(datafile, outfile)

