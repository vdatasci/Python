from BeautifulSoup import BeautifulSoup
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






with open('F:\_\rs\data.txt', 'w') as f:
     f.write(response.read())


