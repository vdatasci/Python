import urllib
import urllib2
from bs4 import BeautifulSoup
import csv
import unicodedata
import re

url = "https://www.youtube.com/playlist?list=PLB2ZDXbXoRXnlW-0AaIEq8rDtToERYoK4"

response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)


with open(r'F:\Python\Projects\Youtube\Music\From_Youtube\Videos_List.csv', 'a') as f:
    for vid in soup.findAll(attrs={'class':'pl-video-title-link'}):
        vidtext = unicodedata.normalize('NFKD', vid.text).encode('ascii','ignore').strip()
        yurl = re.sub('(\&index=)\d+', '', re.sub('(\&list).*', '', 'https://www.youtube.com'+vid['href']))
        f.write(str(vidtext+';'+vidtext+';'+yurl)+'\n')


