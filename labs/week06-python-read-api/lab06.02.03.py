#c005806e957c8813d8b0d98cef207efb06f97a98
#curl -i -H "Authorization: Token token-goes-here" https://api.github.com/repos/osheah/testtoken
import requests, json

url = "https://api.github.com/repos/osheah/testtoken"
apiKey = "token-goes-here"
response=requests.get(url, auth=('token',apiKey))
repoJSON=response.json()
print(response.json())
filename = "testtoken.json"
file=open(filename,'w')
json.dump(repoJSON,file,indent=4)