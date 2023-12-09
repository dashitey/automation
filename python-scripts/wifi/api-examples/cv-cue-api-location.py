import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CV_CUE = "https://awm11013-c4.srv.wifi.arista.com/wifi/api/"
GUEST_MGR = "https://agm11006-c4.srv.wifi.arista.com/api/"


url= CV_CUE
headers = {
    'content-type': "application/json",
    'cookie': 'JSESSIONID=279172378AFB3531D24D57F89FCBDC94'
        }

api = "locations"
payload = ''
response = requests.get(url+api, headers=headers,verify=False)

output = response.json()

print (output)
