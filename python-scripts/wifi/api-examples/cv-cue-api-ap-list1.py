import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CV_CUE = "awm11013-c4.srv.wifi.arista.com/wifi/api/"
#CVP_USER = "arista"
#CVP_PASS = "aristar3r0"

url= "https://%s"%CV_CUE
headers = {
    'content-type': "application/json",
    'authorization': "Bearer 7925f5e86968230f9793e7959c086af3"
            }
loginURL = "/aps"
authenticateData = json.dumps({"locationid": "69", "nodeid":"0", "version":"12"})
response = requests.get(url+loginURL, data=authenticateData,headers=headers,verify=False)

output = response.json()

print (output)