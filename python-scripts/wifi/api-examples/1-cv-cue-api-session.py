import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CV_CUE = "https://awm11008-c4.srv.wifi.arista.com/wifi/api/"
GUEST_MGR = "https://agm11006-c4.srv.wifi.arista.com/api/"

url= CV_CUE
headers = {
    'content-type': "application/json",
        }

api = "session"
payload = json.dumps( {
"type": "apikeycredentials",
"keyId": "KEY-ATN567411-1778",
"keyValue": "07f7cd2840bf20ade4b96167e7b173a0",
"timeout": 3600
   })
response = requests.post(url+api, data=payload, headers=headers,verify=False)

output = response.json()

print (output)
