from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import urllib2
import re


r = requests.get('https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q={}&tbm=nws'.format(query))
soup = BeautifulSoup(r.text, "html.parser")

query = str('grand rapids michigan').replace(' ', '+')


response = requests.get(str(url))
html = response.content
soup = BeautifulSoup(html)

response.url

links = []
for item in soup.find_all('h3', {'class': re.compile('.*(\_HId)')}):
    links.append(item.a['href'])




#price = str(soup.find('span', {'title': re.compile('\d+')}).text)
#description = str(soup.find('div', {'class': 'item-description'}).findChild('p').text)

NId
