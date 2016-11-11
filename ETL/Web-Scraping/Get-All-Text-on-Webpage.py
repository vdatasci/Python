import re
import urllib
import requests
from BeautifulSoup import BeautifulSoup


html = urllib.urlopen('http://checkip.dyndns.org').read()
soup = BeautifulSoup(html)

texts = soup.findAll(text=True)

def visible(element):
     if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
         return False
     elif re.match('<!--.*-->', str(element)):
         return False
     return True

visibletxt = filter(visible, texts)

print(vistexts)



#For this example, we can run a regex on all the text of the website to get the ip address.
#re.search('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+',str(visibletxt)).group(0)


#re.findall('[0-9]+',str(visibletxt))
#can also use finditer


