from urllib.request import urlretrieve
from threading import *
import bs4
import requests
import csv
import os
screenlock=Semaphore(value=1)
database=open("free-zipcode-database-Primary.csv")
grabbedMapFile=open("grabbedMap","a+")
mapRequestUrl="https://www.ups.com/maps/"
reader=csv.DictReader(database)
imgdict=dict()
maplist=set()
grabbedMap=grabbedMapFile.readlines()
def grabber(Database,url,place):
    if place["Zipcode"] in grabbedMap:
        screenlock.acquire()
        print("[+] Already have the map correspond to this zipcode "+place["Zipcode"])
        screenlock.release()
    if os.path.exists("./map/"+place["State"]+place["Zipcode"]+".gif"):
        screenlock.acquire()
        print("[+] Already have the map correspond to this zipcode "+place["Zipcode"])
        grabbedMapFile.write(place["Zipcode"]+"\n")
        screenlock.release()
    if place['State'] == "PR" or place["State"] == "HI":
        screenlock.acquire()
        print("[-] "+i["Zipcode"]+" Not in list")
        grabbedMapFile.write(place["Zipcode"]+"\n")
        screenlock.release()
        return
    else:
        try:
            parameters={"zip":place['Zipcode']}
            map=requests.post(mapRequestUrl,params=parameters)
            map=bs4.BeautifulSoup(map.text,"html.parser")
            imgPage=map.find("img",id="imgMap")["src"]
            imguri="https://www.ups.com"+imgPage
            if imguri in maplist:
                screenlock.acquire()
                print("[+] Already found the map corresponds to this zipcode "+place["Zipcode"])
                grabbedMapFile.write(place["Zipcode"]+"\n")
                screenlock.release()
                return
            else:

                maplist.add(imguri)
                imgdir="./map/"+place["State"]+place["Zipcode"]+".gif"
                urlretrieve(imguri,imgdir)
                screenlock.acquire()
                print("[+] Download successfully on Map "+place["Zipcode"])
                grabbedMapFile.write(place["Zipcode"]+"\n")
                screenlock.release()
        #except (TimeoutError,TypeError,ssl.SSLEOFError) as err:
        except:
            screenlock.acquire()
            print("[-] Zipcode "+place["Zipcode"]+" area cannot use as a warehouse.")# Err code")#+str(err))
            screenlock.release()
            return
for i in reader:
    #print(i['Zipcode'])
    #i={"Zipcode":"02114","State":"NY"}
    grab=Thread(target=grabber,args=(database,mapRequestUrl,i))
    grab.start()
    i=input()
    #grabber(database,mapRequestUrl,i)
print("[+] Finished Grabbing")
with open("location","w") as warehouseLocation:
    warehouseLocation.writelines(maplist)



