from BeautifulSoup import BeautifulSoup
import unicodedata
import requests
import re


url = 'http://www.hotnewhiphop.com/'


response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)




li = soup.findAll('div', {'class': ['cover-title','dailySongChart-artist','dailySongChart-e
ditor-review']})

for l in li:
    print unicodedata.normalize('NFKD', l.text).encode('ascii','igonre')

