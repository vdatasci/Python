from BeautifulSoup import BeautifulSoup
import requests
import numpy
import re

url = 'https://grandrapids.craigslist.org/search/hsw'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

listingtaglist = []
listingtags = soup.findAll("li", {"class" : "result-row"})
for listings in listingtags:
    listingtaglist.append(listings.text)
    print listings.text

pricetagslist = []
pricetags = soup.findAll("span", {"class" : ["result-price"]})
for prices in pricetags:
    pricetagslist.append(prices.text)
    print prices.text


listingsarray = numpy.asarray(listingtaglist)
pricesarray = numpy.asarray(pricetagslist)
masterarray = numpy.column_stack((listingsarray, pricesarray))

masterarray
