import requests

url = "https://192.168.0.21/command-api"
auth = {'username':'arista','password':'arista4pud'}


commands = open("eth1.json", "r")

r = requests.post(url, auth=('arista','arista4pud'), data=commands, verify=False) 

print(r.text)