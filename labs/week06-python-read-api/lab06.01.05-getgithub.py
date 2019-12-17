import requests, json
from xlwt import *
url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()
filename = 'githubusers.json'
with open(filename, 'w') as f:
  json.dump(data, f, indent=4)

w = Workbook()
ws = w.add_sheet('followers')
row = 0
ws.write(row,0,"login") 
ws.write(row,1,"repos_url")


row += 1
for user in data:
  ws.write(row,0,user["login"]) 
  ws.write(row,1,user["repos_url"])
  row += 1 
w.save('githubusers.xls')