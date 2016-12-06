from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import sqlite3
import re



url= 'https://www.youtube.com/feed/trending'


browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url)

response = requests.get(browser.geturl())
html = response.content
soup = BeautifulSoup(html)

#<h3 class="yt-lockup-title ">

ytitles = soup.findAll('h3', {'class': "yt-lockup-title "})
for yt in ytitles:
    print yt.text


linklist = []
for link in links:
    linklist.append(link['href'])
