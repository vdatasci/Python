from BeautifulSoup import BeautifulSoup
import mechanize
import requests
import re


url= 'http://www.w3schools.com/html/html_tables.asp'
url2 = 'http://services.runescape.com/m=itemdb_oldschool/top100?list=0'


browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url2)


response = requests.get(browser.geturl())
html = response.content
soup = BeautifulSoup(html)


table = soup.find('table')
links = table.findAll('a')

linklist = []
for link in links:
    linklist.append(link['href'])


headers = []
for header in table.findAll('th'):
    headers.append(header.text.encode('utf8'))


rows = []
for row in table.findAll('tr'):
    rows.append([val.text.encode('utf8') for val in row.findAll('td')])


del rows[0]


with open('P:\TempFile.txt', 'w') as f:
    f.write(str(', '.join(headers)))


with open("P:\TempFile.txt", "a") as f:
    for r in rows:
        f.write(str(', '.join(r)) + '\n')

