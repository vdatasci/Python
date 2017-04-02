from BeautifulSoup import BeautifulSoup
import unicodedata
import requests
import re


url = 'http://www.hotnewhiphop.com/'


response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)



li = soup.findAll('div', {'class': ['cover-title','dailySongChart-artist','dailySongChart-editor-review']})

lst = []
for l in li:
    lst.append(unicodedata.normalize('NFKD', l.text).encode('ascii','igonre'))


np.resize(lst,(np.matrix(lst).size/3,3))
