import mysql.connector

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  
  )

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE datarepresentation2") # I've already got datarepresentation and am using it for my project