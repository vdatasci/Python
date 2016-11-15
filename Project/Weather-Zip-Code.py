#div class='vk_c card-section'

import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=weather+' + raw_input('ENTER ZIP CODE:  ')

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

pricetagslist = []
pricetags = soup.findAll("div", {"class" : ["vk_c card-section"]})
for prices in pricetags:
	pricetagslist.append(prices.text)
