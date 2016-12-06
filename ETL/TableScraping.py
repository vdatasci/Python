from BeautifulSoup import BeautifulSoup
import mechanize
import requests
import re


url= ''

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url)


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


