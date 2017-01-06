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


items_list = ['','']
item_id = ['1887', '1905', '1277']


for item in item_number:
    url = 'http://services.runescape.com/m=itemdb_oldschool/viewitem?obj=' + item_id

    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)


    name = str(soup.find('div', {'class': 'item-description'}).findChild('h2').text)
    price = str(soup.find('span', {'title': re.compile('\d+')}).text)
    
    



