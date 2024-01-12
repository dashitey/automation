import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CVP_HOST = "192.168.0.5"
CVP_USER = "arista"
CVP_PASS = "arista4i84"

url= "https://%s"%CVP_HOST
headers = { 'Content-Type': 'application/json' }
loginURL = "/cvpservice/login/authenticate.do"
authenticateData = json.dumps({'userid': CVP_USER, 'password': CVP_PASS})
response = requests.post(url+loginURL, data=authenticateData,headers=headers,verify=False)
assert response.ok
cookies = response.cookies
output = response.json()

print ("User Name: %s\n "%output['username'])
print ("First Name: %s\n "%output['user']['firstName'])
print ("Last Name: %s\n "%output['user']['lastName'])
print ("User Permissions: %s\n "%output['permissionList'])
print ("Cookie Jar: %s\n "%cookies)
