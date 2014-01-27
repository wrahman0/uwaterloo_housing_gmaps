#!/usr/bin/env python
import scraperwiki           
import lxml.html           


html = scraperwiki.scrape("https://listings.och.uwaterloo.ca/Listings/Search/Results")
root = lxml.html.fromstring(html)

addressCheck1 = "Waterloo, ON"
addressCheck2 = "waterloo, ON"
addressCheck3 = "Cambridge, ON"
addressCheck4 = "cambridge, ON"
addressCheck5 = "Kitchener, ON"
addressCheck6 = "kitchener, ON"

address = "https://listings.och.uwaterloo.ca/Listings/Search/Results?page="
master = {}
nameList = []
priceList = []
page = 0
numpages = 26

while (page!=numpages):
	#Redirecting to new 
	html = scraperwiki.scrape(address+str(page+1))
	root = lxml.html.fromstring(html)

	#Targeting the names and location
	#Name of the location
	for tr in root.cssselect("div#Rentals tr td span a"):
	    print "Scraping Names Page:" + str(page) + "..."
	    name = str.strip(tr.text_content())
	    if addressCheck1 in name or addressCheck2 in name or addressCheck3 in name or addressCheck4 in name or addressCheck5 in name or addressCheck6 in name:
	       # print name
	        nameList.append(name)
	    
	#Price Listing
	for tr in root.cssselect(".t-last"):
	    print "Scraping Prices Page:" + str(page) + "..."
	    price = str.strip(tr.text_content())
	    price = ''.join(price.split())
	   # print price
	    priceList.append(price)

	page+=1

i = 0
while (i!=len(nameList) and i!=len(priceList)):
    master[nameList[i]] = priceList[i]
    i+=1
    

for location,price in master.items():
	print "Name: " + location +"  ---  " + "Price: " + price
