import urllib
import urllib2
from bs4 import BeautifulSoup

textToSearch = 'hello world'
query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    print 'https://www.youtube.com' + vid['href']

for vcount in soup.findAll(attrs={'class':'yt-lockup-meta-info'}):
    print vcount.text


def syoutube(textToSsearch):
    query = urllib.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    ylist = []
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        ylist.append('https://www.youtube.com' + vid['href'])
    for i in ylist: print i


