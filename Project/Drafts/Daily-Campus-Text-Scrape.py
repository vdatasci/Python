import re
import urllib
import requests
from BeautifulSoup import BeautifulSoup


html = urllib.urlopen('http://dailycampus.com/').read()
soup = BeautifulSoup(html)

texts = soup.findAll(text=True)

def visible(element):
     if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
         return False
     elif re.match('<!--.*-->', str(element)):
         return False
     return True

visibletxt = filter(visible, texts)

print(visibletxt)
