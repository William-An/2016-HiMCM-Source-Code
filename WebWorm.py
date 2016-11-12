from urllib.request import urlretrieve
from threading import *
import bs4
import requests
import csv
screenlock=Semaphore(value=1)
database=open("free-zipcode-database-Primary.csv")
mapRequestUrl="https://www.ups.com/maps/"
reader=csv.DictReader(database)
imgdict=dict()
maplist=set()
def grabber(Database,url,place):
    if place['State'] == "PR":
        screenlock.acquire()
        print("[-] "+i["Zipcode"]+" Not in list")
        screenlock.release()
        return
    else:
        parameters={"zip":place['Zipcode']}
        map=requests.post(mapRequestUrl,params=parameters)
        map=bs4.BeautifulSoup(map.text,"html.parser")
        imgPage=map.find("img",id="imgMap")["src"]
        imguri="https://www.ups.com"+imgPage
        if imguri in maplist:
            return
        else:

            maplist.add(imguri)
            imgdir="./map/"+place["State"]+place["Zipcode"]+".gif"
            urlretrieve(imguri,imgdir)
            screenlock.acquire()
            print("[+] Download successfully on Map "+place["Zipcode"])
            screenlock.release()

for i in reader:
    #print(i['Zipcode'])
    grab=Thread(target=grabber,args=(database,mapRequestUrl,i))
    grab.start()
    #grabber(database,mapRequestUrl,i)



