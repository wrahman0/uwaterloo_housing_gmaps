#!/usr/bin/env python
import scraperwiki           
html = scraperwiki.scrape("https://listings.och.uwaterloo.ca/Listings/Search/Results")
import lxml.html           
root = lxml.html.fromstring(html)
nameList = []

#Targeting the names and location
for tr in root.cssselect("div#Rentals tr td span a"):
    print "_________________________________"
    name = tr.text_content()
    print name
    nameList.extend(name)
    
    
    
#Price Listing

for tr in root.cssselect(".t-last"):
    price = tr.text_content()
    print price
    
##UPDATED AND BETTER TARGETTING

#!/usr/bin/env python
import scraperwiki           
html = scraperwiki.scrape("https://listings.och.uwaterloo.ca/Listings/Search/Results")
import lxml.html           
root = lxml.html.fromstring(html)
master = []
nameList = []
priceList = []
#Targeting the names and location
for tr in root.cssselect("div#Rentals tr td span a"):
    print "_________________________________"
    name = tr.text_content()
    nameList.extend(name)
    
#Price Listing
for tr in root.cssselect(".t-last"):
    price = tr.text_content()
    priceList.extend(price)
    
i = 0
while(i!=len(nameList) or i!=len(priceList)):
    temp = {"Name" : nameList[i],
              "Price": priceList[i]
             }
    print temp
    master.extend(temp)
    i+=1

# j = 0
# while (j != len(master)):
#     print master[j]
#     j+=1
    

