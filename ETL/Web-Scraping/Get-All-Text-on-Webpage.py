import re
import urllib
import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.youtube.com/feed/trending'
url2 = 'http://checkip.dyndns.org'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

texts = soup.findAll(text=True)

def visible(element):
     if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
         return False
     elif re.match('<!--.*-->', str(element)):
         return False
     return True

visibletxt = filter(visible, texts)

print(visibletxt.encode('utf8'))



#For this example, we can run a regex on all the text of the website to get the ip address.
#re.search('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+',str(visibletxt)).group(0)


#re.findall('[0-9]+',str(visibletxt))
#can also use finditer


