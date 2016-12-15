from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import sqlite3
import re


url = 'http://www.tradingeconomics.com/commodities'

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url)
response = requests.get(browser.geturl())
html = response.content
soup = BeautifulSoup(html)


len(soup.findAll('table'))

