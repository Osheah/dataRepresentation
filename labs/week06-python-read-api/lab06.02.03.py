#c005806e957c8813d8b0d98cef207efb06f97a98
#curl -i -H "Authorization: Token c005806e957c8813d8b0d98cef207efb06f97a98" https://api.github.com/user/repos
import requests, json

url = "https://api.github.com/repos/Osheah/dataRepresentation"
apiKey = "add token key here"
response=requests.get(url, auth=('token',apiKey))
repoJSON=response.json()
#print(response.json())
filename = "osheah"
file=open(filename,'w')
json.dump(repoJSON,file,indent=4)