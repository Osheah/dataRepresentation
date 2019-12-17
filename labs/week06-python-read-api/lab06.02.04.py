import requests
import json
url = "https://api.github.com/repos/datarepresentationstudent/aPrivateOne"
apiKey = "f9c62db8c4745152c4e580d1a8e2938a90501495"
url2="https://api.github.com/repos/datarepresentationstudent/aPrivateOne/collaborators/"

dataString = {url2: "Osheah"}

 
response = requests.put(url, json=dataString, auth=('token',apiKey)) 
repoJSON = response.json()
dataString = {}
print(repoJSON)

## not working - come back to this later if time