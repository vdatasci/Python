import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import requests
from BeautifulSoup import BeautifulSoup
import re
import webbrowser
import os


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


print('')
for i in range(len(titles)):
     ans = raw_input("Do you want to read about " + titles[i] + "?")
     if fuzz.partial_ratio(ans, "Yes") > 50:
		 soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki?curid=' + ids[i]).content)
		 result = soup.find("div", {"id":"mw-content-text"}).find('p').text
		 print(result)
		 os.system('P:\Python\Projects\wiki_v2.py')
