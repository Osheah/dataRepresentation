import requests
import json
url = "https://api.github.com/repos/datarepresentationstudent/aPrivateOne"
apiKey = "c005806e957c8813d8b0d98cef207efb06f97a98"
dataString = {"private": "false"}


response = requests.put(url, json=dataString, auth=('token',apiKey)) 
repoJSON = response.json()

print(response.json())