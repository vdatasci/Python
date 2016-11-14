import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.mygrocerydeals.com/deals?utf8=%E2%9C%93&authenticity_token=m3GcOr5X%2BII7qWKA6RVd%2BIm8XtJW5nINqZje4NMCees%3D&remove%5B%5D=chains&remove%5B%5D=categories&remove%5B%5D=collection&remove%5B%5D=collection_id&q=&supplied_location=storrs%2C+ct&latitude=41.8084314&longitude=-72.24952309999997&order%5Bdirection%5D=asc&order%5Bvalue%5D=sale_end&q=noodles'



response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

pricetagslist = []
pricetags = soup.findAll("span", {"class" : ["pricetag pricetag-md","pricetag pricetag-lg","pricetag"]})
for prices in pricetags:
	pricetagslist.append(prices.text)

productnameslist = []
productnames = soup.findAll("p", {"class" : "deal-productname"})
for product in productnames:
	productnameslist.append(product.text)


import numpy
productsarray = numpy.asarray(productnameslist)
pricesarray = numpy.asarray(pricetagslist)
masterarray = numpy.column_stack((productsarray, pricesarray))
numpy.savetxt("P:\TempFile.txt", masterarray, delimiter=" | ", fmt="%s")


### APPENDING TO TEXTFILE
# f_handle = file('my_file.dat', 'a')
# savetxt(f_handle, my_matrix)
# f_handle.close()

