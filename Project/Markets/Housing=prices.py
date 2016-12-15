from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import sqlite3
import re

url= 'https://www.trulia.com/MI/Grand_Rapids/'

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url)
response = requests.get(browser.geturl())
html = response.content
soup = BeautifulSoup(html)

raw_hdata = soup.findAll('div', {'class':'cardDetails man ptm phm'})

for hd in raw_hdata:
    print re.search(str(hd.text)0, '(\$\d+\,\d+|\$\d+\,\d+)').group(0)



