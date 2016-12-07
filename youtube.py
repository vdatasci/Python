import re
import urllib
import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.youtube.com/feed/trending'
url2 = 'http://checkip.dyndns.org'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

linklist = []
ytitles = soup.findAll('div', {'class': 'yt-lockup-content'})
for yt in ytitles:
        linklist.append(str(re.search('.*(?=Duration)', ytitles[10].text[1:-1]).group(0)))
