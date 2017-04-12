import urllib
import urllib2
from bs4 import BeautifulSoup

url = "https://www.youtube.com/playlist?list=PLB2ZDXbXoRXnlW-0AaIEq8rDtToERYoK4"

response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)

vids = []
for vid in soup.findAll(attrs={'class':'pl-video-title-link'}):
    vids.append(vid['href'])
