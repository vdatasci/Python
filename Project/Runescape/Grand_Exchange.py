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


url='http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=21787'

response = urllib2.urlopen(url)
data = json.loads(str(response.read()))

name = str(data['item']['name'])
price = str(data['item']['current']['price'])


with open('F:\\_\\rs\\items-data.csv', 'w') as f:
     f.write(name + ', ' + price + '\n')






df = pd.DataFrame([[name, price]])
df.columns = ['item', 'price']

df




with open('F:\_\rs\data.txt', 'w') as f:
     f.write(response.read())


