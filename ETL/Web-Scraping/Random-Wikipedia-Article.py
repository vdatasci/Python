import requests
from BeautifulSoup import BeautifulSoup
import re


url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=xml'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

ids = []
for item in soup.findAll(id=re.compile("[0-9]")):
     ids.append(item['id'])
     
titles = []
for name in soup.findAll(title=re.compile(".*")):
     titles.append(name['title'])


mat = [ids, titles]
zip(*mat)