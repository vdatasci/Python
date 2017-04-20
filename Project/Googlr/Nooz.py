from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import urllib2
import re


goos = str('grand rapids michigan')

#goos = raw_input('Search Google:   ')


url = 'https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=' + goos.replace(' ', '+') + str('&tbm=nws')


response = requests.get(str(url))
html = response.content
soup = BeautifulSoup(html)

response.url

links = []
for item in soup.findAll('h3', {'class': re.compile('.*( _U6c)'}):
    links.append(item.a['href'])




#price = str(soup.find('span', {'title': re.compile('\d+')}).text)
#description = str(soup.find('div', {'class': 'item-description'}).findChild('p').text)

NId
