import bs4
import requests
import csv
database=open("free-zipcode-database-Primary.csv")
mapRequestPage="https://www.ups.com/maps/"
reader=csv.DictReader(database)
for i in reader:
    #print(i['Zipcode'])
    parameters={"zip":'03101'}
    map=requests.post(mapRequestPage,params=parameters)
    print(map.text)
    map=bs4.BeautifulSoup(map.text,"html.parser")
    print(map)
    input()
    img=map.find_all("img",id="imgMap")
    print(img)



