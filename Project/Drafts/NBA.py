from BeautifulSoup import BeautifulSoup
import requests
import re


url = 'https://sports.yahoo.com/nba/teams/nyk/roster/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)


for playerlink in soup.findAll('a', href=re.compile('^.*/players/([0-9]+)')):
    print playerlink.text
    print playerlink['href']
    print '\n'




for playerlink in soup.findAll('table', summary=re.compile('Player')):
    a = str(playerlink.contents).encode('ascii','ignore').replace('\n', '')

with open('P:\\TempFile.txt', 'w') as f:
    f.write(a)
