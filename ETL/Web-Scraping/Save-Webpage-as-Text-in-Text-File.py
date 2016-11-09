import urllib2


url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=xml'
response = urllib2.urlopen(url)

with open('P:\output.txt', 'w') as f:
     f.write(response.read())

     
     
     

###     
import requests
from BeautifulSoup import BeautifulSoup
import re


url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=xml'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

ids = []
for item in soup.findAll(id=re.compile("[0-9]")):
     id.append(item['id'])
