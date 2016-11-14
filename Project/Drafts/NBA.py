import requests
from BeautifulSoup import BeautifulSoup

url = 'https://sports.yahoo.com/nba/teams/nyk/roster/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

import re
soup.findAll('a', href=re.compile('^/players/'))





