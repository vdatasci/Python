import re
import urllib
import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.youtube.com/feed/trending'
url2 = 'http://checkip.dyndns.org'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

cont = soup.findAll('h3', {'class': 'yt-lockup-title'})
for c in cont:
    print str(c.text)


#cont = soup.find('div', {'id': 'content'})
#cont
