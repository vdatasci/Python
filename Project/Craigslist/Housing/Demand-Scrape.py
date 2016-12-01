from BeautifulSoup import BeautifulSoup
import requests
import numpy
import re


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


url = 'https://grandrapids.craigslist.org/search/hsw'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

listingtaglist = []
listingtagprice = []
listingtags = soup.findAll("li", {"class" : "result-row"})
for listings in listingtags:
    descr = listings.text
    listingtaglist.append(descr)
    prc = re.search('(\$\d+|\s)', descr).group(0)
    listingtagprice.append(prc)
        
        



masterarray = []
listingsarray = numpy.asarray(listingtaglist)
pricesarray = numpy.asarray(pricetagslist)

print(listingsarray.size)
print(pricesarray.size)

#masterarray = numpy.column_stack((listingsarray, pricesarray))

#numpy.savetxt("P:\TempFile.txt", masterarray, delimiter=" | ", fmt="%s")






#pricetagslist = []
#pricetags = soup.findAll("span", {"class" : ["result-price"]})
#for prices in pricetags:
#    pricetagslist.append(prices.text)
#    print prices.text
