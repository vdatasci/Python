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



item_number = [1887]

url = 'http://services.runescape.com/m=itemdb_oldschool/viewitem?obj=' + item_number

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)



soup.findAll("class", {"class" : "result-row"})

