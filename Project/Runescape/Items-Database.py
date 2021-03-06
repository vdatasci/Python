from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import urllib2
import sqlite3
import json
import csv
import re




items_list = np.array(['','',''])
i = ['1887', '1905', '1277', '0', '1', '229']
item_numbers = list(xrange(25000))


for item_id in item_numbers:
    url = 'http://services.runescape.com/m=itemdb_oldschool/viewitem?obj=' + str(item_id)
    response = requests.get(str(url))
    html = response.content
    soup = BeautifulSoup(html)
    try:
        name = str(soup.find('div', {'class': 'item-description'}).findChild('h2').text)
        price = str(soup.find('span', {'title': re.compile('\d+')}).text)
        description = str(soup.find('div', {'class': 'item-description'}).findChild('p').text)
        new_row = np.array((name + ',' + price + ',' + description).split(','))
        items_list = np.vstack((items_list,new_row))
    except AttributeError:
        continue

        
items_list = np.delete(items_list, (0), axis=0)
items_list
    
    

