import requests
import json
from xlwt import *
url = 'https://api.github.com/users/andrewbeattycourseware/followers'
#response = requests.get(url)
#data = response.json()
# token  c005806e957c8813d8b0d98cef207efb06f97a98
#print(data)
# get the file name for the new file to write
#filename = 'githubusers.json'
#with open(filename,'w') as f: 
#  json.dump(data, f, indent = 4)
w = Workbook()
ws = w.add_sheet('followers')
row = 0; 
ws.write(row, 0, "login")
ws.write(row, 1, "repos_url")    
row +=1

#print(data[0:1])

for follower in data["followers"]:
  ws.write(row, 0, data['login'])
  ws.write(row, 1, data['repos_url']) 
  row +=1
w.save('githubusers.xls')