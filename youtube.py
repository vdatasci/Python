import urllib
import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.youtube.com/feed/trending'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

linklist = []
ytitles = soup.findAll('div', {'class': 'yt-lockup-content'})
for yt in ytitles:
    linklist.append(BeautifulSoup(str(yt)).find(text=True))

linklist
