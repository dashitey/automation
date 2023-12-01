import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CVP_HOST = "192.168.0.5"
#CVP_USER = "arista"
#CVP_PASS = "aristar3r0"

url= "https://%s"%CVP_HOST
headers = {
    'content-type': "application/json",
    'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjcyMTAzNzUyOTEwNDUxNTA4NDEsImRzbiI6ImFyaXN0YSIsImRzdCI6InVzZXIiLCJleHAiOjE3MDE0ODEzMjIsImlhdCI6MTcwMTM5NDkyMiwic2lkIjoiMDI3NzcwODgzZDA0MTZiNzA0MDkzNmE3YWIyYThkNmIwNzY1ZGM5ZTU3MzA0MDE0MGVjYzYyZTZhNzgzNzYxNC1RaUNJWFdxVTYyTE9ZQnFNd1piVkM5NDJGa2c3WGxWbWtLNS1SN24tIn0.Z7dhujUm2F9x_ZJfZs3-xYsgs2b4FR_TAogaUFfnVf2BtRhMjHKNrwebVpApEWw9vqEevCcEy1C-O7Vln1LrthzXFjYuG8K2rmcs01-WKKdFOlf1vr3jL7X4UR7ox4MfiWedwAh02eNIyDH2JZ5bdQ8WNzAUxbxPoxOPcYlfu4cE6BUGuylP01FJhoewEgjO2Gw7bLqe0ROvnVut0s0-4gg2pE1Y78l7maKxzUBHQSa8Ab2u9aZO1q47uDiD68IAq1ItoQ8JYyOHxvnnFNhy_3HgrXAPT2QS8D0UC8y0DDnydobXRmGfyT0bsU_14_aW65Mos-2updaNm8vQt75CERZgM1GTGyKRrXe3s_f8RaawyyGigs3J2gaMJBNb6kuLYfiZBzuAxPT8ouycCDW5u--ZLpy6aEJPyFWZ_JJkMIOuOu7EIvNwUbXpRPvyk3F2iFYYXXg2X3031OZSP5Zi-DIiRiCO698_7YwXhaChbXqU_aRkdJR4f0U_PKBB8cmVus-2McLRh_j69J-T3EEGRcNSE4uFisQfC2B5lIUnn8iEDt-8oxq7EQj3SOP76QafteQ1vwl_lque3jWESiye-HDihJVsfIiWuLon6GK6VGpyZLvqPL-KQTFg8tnadh3fJsVveusn09T9otHcJB9p43_9XuyZURt655jN0hyE3w0"
        }
loginURL = "/cvpservice/inventory/devices"
authenticateData = json.dumps({"": ""})
response = requests.get(url+loginURL, data=authenticateData,headers=headers,verify=False)
#assert response.ok
#cookies = response.cookies
output = response.json()

print (output)