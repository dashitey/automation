import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CV_CUE = "https://awm11008-c4.srv.wifi.arista.com/wifi/api/"
GUEST_MGR = "https://agm11006-c4.srv.wifi.arista.com/api/"


url= CV_CUE
headers = {
    'content-type': "application/json",
    'cookie': 'JSESSIONID=F9A7BDF5E3A7134F6FC22DED86EE22DB'
        }

api = "clients"
payload = ''
response = requests.get(url+api, headers=headers,verify=False)

output = response.json()

print (output)
