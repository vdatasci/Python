import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import requests
from BeautifulSoup import BeautifulSoup
import re
import webbrowser


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



for i in range(len(titles)):
     ans = raw_input("Do you want to read about " + titles[i] + "?")
     if fuzz.partial_ratio(ans, "Yes") > 75:
          url = 'https://en.wikipedia.org/wiki?curid=' + ids[i]
          webbrowser.open(url,new=1)

#for i in range(len(titles)):
     #if process.extract(input("Do you want to read about " + titles[i] + "?"), choices, limit=1) == choice[0]:
          #url = 'https://en.wikipedia.org/wiki?curid=' + ids[i]
     #else:
          #break
     
     
     #if process.extract(raw_input, choices, limit=1) = 'Yes'
          #url = 'https://en.wikipedia.org/wiki?curid=' + ids[i]
          #continue
     
 


#mat = [ids, titles]
#zip(*mat)
