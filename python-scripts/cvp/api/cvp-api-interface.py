import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CVP_HOST = "192.168.0.5"
CVP_USER = "arista"
CVP_PASS = "arista4pud"

url= "https://%s"%CVP_HOST
headers = { 'Content-Type': 'application/json' }
loginURL = "/cvpservice/provisioning/devices"
authenticateData = json.dumps({"deviceId": "string"})
response = requests.post(url+loginURL, data=authenticateData,headers=headers,verify=False)
# assert response.ok
cookies = response.cookies
output = response.json()

print (output)