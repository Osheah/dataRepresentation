import requests
import json
import datetime
from datetime import date, timedelta
from xlwt import *

with open('dateRow.json') as fp: 
    #dateToSearch="2019-11-10"
    dateRow = json.load(fp)
    dateToSearch = dateRow['Date']
    rowNumber = dateRow['rowNumber']

#print(dateToSearch, rowNumber)
#print(rowNumber)
#url = "https://reports.sem-o.com/api/v1/documents/static-reports"

url= "https://reports.sem-o.com/api/v1/documents/static-reports?rtName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>"+dateToSearch
#print (url)
response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"]
#print (totalPages)
listOfReports = []

pageNumber=1
while pageNumber <= totalPages:
    pageUrl = url + "&page="+ str(pageNumber)
    #print (pageUrl)
    data = requests.get(pageUrl).json()
    for item in data["items"]:
        #print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])

    pageNumber +=1





w = Workbook()
ws = w.add_sheet('report')
#rowNumber = 0;
ws.write(rowNumber,0,"StartTime")
ws.write(rowNumber,1,"EndTime")
ws.write(rowNumber,2,"ImbalanceVolume")
ws.write(rowNumber,3,"ImbalancePrice")
ws.write(rowNumber,4,"ImbalanceCost")
rowNumber += 1 

for ReportName in listOfReports:
    #print(ReportName)
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    #print(url)
    response= requests.get(url)
    aReport= response.json()
    try:              
        for row in aReport["rows"]:
            #print (row)
            #print(row["ImbalancePrice"])
            
            if "StartTime" in row:
                ws.write(rowNumber,0,row["StartTime"])
            if "EndTime" in row:    
                ws.write(rowNumber,1,row["EndTime"])
            if "ImbalanceVolume" in row:
                ws.write(rowNumber,2,row["ImbalanceVolume"])
            if "ImbalancePrice" in row:
                ws.write(rowNumber,3,row["ImbalancePrice"])
            if "ImbalanceCost" in row:
                ws.write(rowNumber,4,row["ImbalanceCost"])
            rowNumber += 1
            w.save('balance.xls') 
            #print(row)
    except:
        print("")
filename ='allReports.json'
f = open(filename, 'w')
json.dump(data,f,indent=4)
x=(datetime.datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d") # code wont run with todays date as there is no info se yesterdays date
dateString = {"Date":x, "rowNumber": rowNumber}
json.dump(dateString, open("dateRow.json", 'w'), indent=4)







