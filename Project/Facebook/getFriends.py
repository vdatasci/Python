from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import sqlite3
import re



url= 'file:///C:/Users/jav11008/Desktop/Teresa%20Cramer.html'

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url)

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

links = soup.findAll('a', {'href': re.compile('.*(fref=pb&hc_location=friends_tab).*')})

links[0]




