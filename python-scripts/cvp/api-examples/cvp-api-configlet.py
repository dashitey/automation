import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CVP_HOST = "192.168.0.5"
#CVP_USER = "arista"
#CVP_PASS = "arista4i84"

url= "https://%s"%CVP_HOST
headers = {
    'content-type': "application/json",
    'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjcyMTAzNzUyOTEwNDUxNTA4NDEsImRzbiI6ImFyaXN0YSIsImRzdCI6InVzZXIiLCJleHAiOjE3MDUxMzcxNzMsImlhdCI6MTcwNTA1MDc3Mywic2lkIjoiNjQ2NDlhY2Y3N2U1Y2I0MzJiOGQ4MTg1ZDZhZGZmODc1N2U0N2I0ZGE0NDVlYjE5YTc1MjYyZjkxNDMxMmI2Ni12aXlJODZrdVVaRUF1clRERlJLaUFrVTZfZzg0aUV2eWQ3VWhIU2Y2In0.qVliI-H9iTwDUdpIEkrhltoBCkO_gH0wzU1gzzZgZee8MzNXXDFdBzx-e9tpQhlOqLobP7wuZFqeDrQGx2B9fvvFdWzrazoyvI_4rSqmQHYN0GkiM70BF68_p8KqhsgTirn_4ufK-OwG8z1ujvhC4VyBkuQAjfMgpLzSLU2-73fX3pb9HNHj1WYAu-Ree-g--x0yt011Fpb1MzOb1KIa0Lxo9nAzT8bH_hOKLNzUegSgY9_wHugPMunGsfyJ5eRb_AFi6gmSCiWWw1Y4xtmApO7YX4zZ5Iwdi5jYYtINYC-m4gNdH3QOMzcifNLNol5ACAFkb_7dUAKtUsEcLfA_6ONx527sRbAKGqZEiK1DuPcPjNHwh3bwfpfYeXvaCg5ppMzahrwDtB01tEMp1ugbrfHeqk2MI-r3lQQhlD2AUGbusRk7MUF7qs42AfqZkgvPIN4xtgvANawa0DwNweQTJHUk9x2R6REJj6Uk7ZUFiTdEc3Es5k6Juc6YfjY0VOo9IoFVQU6l83qNgNAQ-l7LDq0-klek6JEABtPA1H951Llqj16BUxaksr_FNyok8NYqSXHD6KiJPCSThzNZCZlD0-lm6K5At60FtK0VdqgKxFmQ6K4f2Geb0vUfIOjVA-7NNKMIahJgGvJA6axuwJvNeAgSGSpNS99Hq46dC7M65lc"
        }

loginURL = "/cvpservice/configlet/addConfiglet.do"
authenticateData = json.dumps({"config": "sample configlet4",  "name": "test3"})
response = requests.post(url+loginURL, data=authenticateData,headers=headers,verify=False)

output = response.json()

print (output)
