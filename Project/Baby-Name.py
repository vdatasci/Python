import re
import urllib
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://api.genderize.io/?name=' + raw_input('ENTER BABY NAME:  ')

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

re.search('(?<=\"gender":\")\w+', str(soup.contents)).group(0)

raw_input()
