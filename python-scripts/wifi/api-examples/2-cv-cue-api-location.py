import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CV_CUE = "https://awm11013-c4.srv.wifi.arista.com/wifi/api/"
GUEST_MGR = "https://agm11006-c4.srv.wifi.arista.com/api/"


url= CV_CUE
headers = {
    'content-type': "application/json",
    'cookie': 'JSESSIONID=6B1956376651F22F6E9F5E2E24C63CD9'
        }

api = "locations"
payload = ''
response = requests.get(url+api, headers=headers,verify=False)

output = response.json()

print (output)
