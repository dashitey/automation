import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CV_CUE = "https://awm11013-c4.srv.wifi.arista.com/wifi/api/"
GUEST_MGR = "https://agm11006-c4.srv.wifi.arista.com/api/"
TOKEN = "Bearer 7925f5e86968230f9793e7959c086af3"

url= CV_CUE
headers = {
    'content-type': "application/json",
    'authorization': 'TOKEN'
        }

loginURL = "/aps"
authenticateData = json.dumps({"locationid": "69", "nodeid":"0", "version":"12"})
response = requests.get(url+loginURL, data=authenticateData, headers=headers,verify=False)

output = response.json()

print (output)
