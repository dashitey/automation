import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CVP_HOST = "192.168.0.5"
CVP_USER = "arista"
CVP_PASS = "arista4pud"

url= "https://%s"%CVP_HOST
headers = { 'Content-Type': 'application/json' }
loginURL = "/cvpservice/inventory/containers"
authenticateData = json.dumps({'userid': CVP_USER, 'password': CVP_PASS})
response = requests.get(url+loginURL, data=authenticateData,headers=headers,verify=False)
#assert response.status_code == 200
#assert response.ok
#cookies = response.cookies
output = response.json()

print (output)
