from urllib.request import urlretrieve
from threading import *
import bs4
import requests
import csv
import os
screenlock=Semaphore(value=1)
database=open("free-zipcode-database-Primary.csv")
mapRequestUrl="https://www.ups.com/maps/"
reader=csv.DictReader(database)
maplist=set()                                          #Store the map we have already visited
def grabber(Database,url,place):
    if os.path.exists("./map/"+place["State"]+place["Zipcode"]+".gif"):                     #Check if we already get the map
        screenlock.acquire()
        print("[+] Already have the map correspond to this zipcode "+place["Zipcode"])
        screenlock.release()
    if place['State'] == "PR" or place["State"] == "HI":                                     #Discard zipcode of HI and PR
        screenlock.acquire()
        print("[-] "+i["Zipcode"]+" Not in list")
        screenlock.release()
        return
    else:
        try:                                                                                   #Try to download the map
            parameters={"zip":place['Zipcode']}
            map=requests.post(mapRequestUrl,params=parameters)
            map=bs4.BeautifulSoup(map.text,"html.parser")
            imgPage=map.find("img",id="imgMap")["src"]
            imguri="https://www.ups.com"+imgPage
            if imguri in maplist:                                                              #If we have already find the map, skip this zipcode
                screenlock.acquire()
                print("[+] Already found the map corresponds to this zipcode "+place["Zipcode"])
                screenlock.release()
                return
            else:                                                                              #Else we retrieve the map

                maplist.add(imguri)
                imgdir="./map/"+place["State"]+place["Zipcode"]+".gif"
                urlretrieve(imguri,imgdir)
                screenlock.acquire()
                print("[+] Download successfully on Map "+place["Zipcode"])
                screenlock.release()
        #except (TimeoutError,TypeError,ssl.SSLEOFError) as err:
        except:                                                                                #Any Error?
            screenlock.acquire()
            print("[-] Zipcode "+place["Zipcode"]+" area cannot use as a warehouse.")# Err code")#+str(err))
            screenlock.release()
            return
for i in reader:
    #print(i['Zipcode'])
    #i={"Zipcode":"02114","State":"NY"}
    grab=Thread(target=grabber,args=(database,mapRequestUrl,i))                                 #Using Thread in threading module to improve performance and speed
    grab.start()
    #i=input()
    #grabber(database,mapRequestUrl,i)
print("[+] Finished Grabbing")
database.close()
with open("location","w") as warehouseLocation:
    for i in maplist:
        warehouseLocation.write(i+"\n")               #Store the uri of the maps we grab




