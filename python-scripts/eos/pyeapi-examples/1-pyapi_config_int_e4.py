# Import the pyeapi library
import pyeapi

pyeapi.load_config('nodes.conf')

switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4']

# Open a session with leaf1


for switch in switches:
    connect = pyeapi.connect_to(switch)
    connect.api("ipinterfaces").create('Ethernet4')
    result = connect.api("ipinterfaces").set_address('Ethernet4','4.4.4.4/24')
    if result == True:
        print("Completed")
    if result == False:
        print("Error")