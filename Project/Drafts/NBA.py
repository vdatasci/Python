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




