from BeautifulSoup import BeautifulSoup
import mechanize
import requests
import urllib2
import json
import re


url='http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=21787'

response = urllib2.urlopen(url)

with open('F:\_\rs\data.txt', 'w') as f:
     f.write(response.read())
