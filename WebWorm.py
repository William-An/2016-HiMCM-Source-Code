import bs4
import csv
database=open("free-zipcode-database-Primary.csv")
mapPage="https://www.ups.com/maps/"
reader=csv.DictReader(database)
for i in reader:
    print(i['Zipcode'])



