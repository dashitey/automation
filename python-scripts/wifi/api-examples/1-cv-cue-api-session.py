import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CV_CUE = "https://awm11013-c4.srv.wifi.arista.com/wifi/api/"
GUEST_MGR = "https://agm11006-c4.srv.wifi.arista.com/api/"

url= CV_CUE
headers = {
    'content-type': "application/json"
        }

api = "session"
payload = json.dumps( {
"type": "apikeycredentials",
"keyId": "your key-id",
"keyValue": "your key-value",
"timeout": 3600
   })
response = requests.post(url+api, data=payload, headers=headers,verify=False)

output = response.json()

print (output)
