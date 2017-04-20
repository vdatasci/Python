from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import urllib2
import re


sgoo = raw_input('Search Google:   ')

raw_input(' ')

url = 'https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q='+sgoo.replace(' ', '+')


response = requests.get(str(url))
html = response.content
soup = BeautifulSoup(html)

response.url

try:
    NId = str(soup.find('div', {'class': '_NId'}).text)
    price = str(soup.find('span', {'title': re.compile('\d+')}).text)
    description = str(soup.find('div', {'class': 'item-description'}).findChild('p').text)
    new_row = np.array((name + ',' + price + ',' + description).split(','))
    items_list = np.vstack((items_list,new_row))
except AttributeError:
    continue


NId
