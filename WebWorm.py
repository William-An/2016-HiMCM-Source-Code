import bs4
import requests
import csv
from urllib.request import urlretrieve
database=open("free-zipcode-database-Primary.csv")
mapRequestPage="https://www.ups.com/maps/"
reader=csv.DictReader(database)
imgdict=dict()
for i in reader:
    #print(i['Zipcode'])
    parameters={"zip":i['Zipcode']}
    map=requests.post(mapRequestPage,params=parameters)
    map=bs4.BeautifulSoup(map.text,"html.parser")
    imgPage=map.find("img",id="imgMap")["src"]
    imguri="https://www.ups.com"+imgPage
    imgdir="./map/"+i["State"]+i["Zipcode"]+".gif"
    urlretrieve(imguri,imgdir)
    print("[+] Download successfully on Map "+i["Zipcode"])




