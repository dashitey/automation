# Import the pyeapi library
import pyeapi
pyeapi.load_config('nodes.conf')
switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4']

# Open a session with leaf1 
connect = pyeapi.connect_to('leaf1')

# "Create" sets the port as a Layer 3 port (no switchport)
connect.api("ipinterfaces").create('Ethernet3')

# Set Ethernet3 for the IP address of 3.3.3.3 and put the result into the variable (boolean) result
result = connect.api("ipinterfaces").set_address('Ethernet3','3.3.3.3/24')

# Very basic error handling here, basically gives a yes or no answer. 
if result == True:
    print("Completed!")

if result == False:
    print("Error!")