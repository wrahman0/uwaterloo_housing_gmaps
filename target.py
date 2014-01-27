#!/usr/bin/env python
import scraperwiki           
import lxml.html           
html = scraperwiki.scrape("https://listings.och.uwaterloo.ca/Listings/Search/Results")
root = lxml.html.fromstring(html)
master = []
nameList = []
priceList = []
addressCheck = "Waterloo, ON"
address = "https://listings.och.uwaterloo.ca/Listings/Search/Results?page="
page = 0

while (page!=7):
	#Redirecting to new 
	html = scraperwiki.scrape(address+str(page+1))
	root = lxml.html.fromstring(html)

	#Targeting the names and location
	for tr in root.cssselect("div#Rentals tr td span a"):
	    name = str.strip(tr.text_content())
	    if addressCheck in name:
	        print name
	        nameList.append(name)
	    
	#Price Listing
	for tr in root.cssselect(".t-last"):
	    price = str.strip(tr.text_content())
	    price = ''.join(price.split())
	    # print price
	    priceList.append(price)

	page+=1
    
    
i = 0
while(i!=len(nameList) and i!=len(priceList)):
    temp = {"Name" : nameList[i],
              "Price": priceList[i]
             }
    print temp
    master.append(temp)
    i+=1

    

