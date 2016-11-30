from BeautifulSoup import BeautifulSoup
import requests
import re

url = 'https://grandrapids.craigslist.org/search/hsw'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

pricetagslist = []
pricetags = soup.findAll("span", {"class" : ["result-price"]})
for prices in pricetags:
    pricetagslist.append(prices.text)
    print prices.text
