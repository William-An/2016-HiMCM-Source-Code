import bs4
import requests
import csv
database=open("free-zipcode-database-Primary.csv")
mapRequestPage="https://www.ups.com/maps/"
reader=csv.DictReader(database)
for i in reader:
    #print(i['Zipcode'])
    parameters={zip:"i"}
    map=requests.post(mapRequestPage,params=parameters)
    print(map.text)



