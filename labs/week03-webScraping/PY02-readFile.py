#this (py02) wasn't mentioned in the lab pdf so its under py01 but its in your code section on github so i'm putting it here 

from bs4 import BeautifulSoup

with open("../week02/carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())