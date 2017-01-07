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


items_list = np.array(['',''])
item_numbers = ['1887', '1905', '1277']


for item_id in item_numbers:
    url = 'http://services.runescape.com/m=itemdb_oldschool/viewitem?obj=' + item_id
    response = requests.get(str(url))
    html = response.content
    soup = BeautifulSoup(html)
    name = str(soup.find('div', {'class': 'item-description'}).findChild('h2').text)
    price = str(soup.find('span', {'title': re.compile('\d+')}).text)
    new_row = np.array((name + ',' + price).split(','))
    items_list = np.vstack((items_list,new_row))
    
    



