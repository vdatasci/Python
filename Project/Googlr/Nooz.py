from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import urllib2
import re


query = str('grand rapids michigan').replace(' ', '+')

result = requests.get('https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q={}&tbm=nws'.format(query))

result.url
result.status_code
result.headers

content = result.content

soup = BeautifulSoup(content, "html.parser")

links = []
for item in soup.find_all('h3', {'class': 'r _U6c'}):
    links.append(item.a['href'])




#price = str(soup.find('span', {'title': re.compile('\d+')}).text)
#description = str(soup.find('div', {'class': 'item-description'}).findChild('p').text)

