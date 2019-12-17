from github import Github
import requests
#remove the minus sign from the key
 
g = Github("f9c62db8c4745152c4e580d1a8e2938a90501495") # other key was bad cred
for repo in g.get_user().get_repos():
  print(repo.name)
repo = g.get_repo("datarepresentationstudent/aPrivateOne")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)
newContents = contentOfFile+"morestuff - hos\n"
print(newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updatedbyprog",newContents,fileInfo.sha)
print(gitHubResponse)