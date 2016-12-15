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
ponse_seek_wrapper at 0x612ab20 whose wrapped object = <closeable_response at 0x612a9b8 who
p = <socket._fileobject object at 0x0612B230>>>
response = requests.get(browser.geturl())
html = response.content
soup = BeautifulSoup(html)

raw_hdata = soup.findAll('div', {'class':'cardDetails man ptm phm'})

for hd in raw_hdata:
    print hd.text

