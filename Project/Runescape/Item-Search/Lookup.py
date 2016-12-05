from BeautifulSoup import BeautifulSoup
import mechanize
import requests
import re


browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open("http://services.runescape.com/m=itemdb_oldschool/top100?list=0")


for form in browser.forms():
    print "Form name:", form.name
    print form


browser.form = list(browser.forms())[0]


for control in browser.form.controls:
    print control
    print control.type
    print '\n'

#squery = browser.form.find_control("query").value
#squery = 'iron'

#browser.submit()
print browser.geturl()



response = requests.get(browser.geturl())
html = response.content
soup = BeautifulSoup(html)


table = soup.find('table')
links = table.findAll('a')
for link in links:
    print link['href']

for row in table.tbody.findAll('tr'):
    first_column = row.findAll('th')[0].contents
    third_column = row.findAll('td')[2].contents
    print first_column, third_column







rows=list()
for row in table.findAll("tr"):
   rows.append(row)



ilist = []
for ilink in soup.findAll('a', href=True):
    ilist.append(ilink['href'])

searchterm = '7936'
pos_in_ilist = [i for i, x in enumerate(ilist) if re.search(searchterm, x)]
pos_in_ilist









#for ilink in soup.findAll('a', {'class':'table-item-link'}):
#    print ilink
    
#for ilink in soup.findAll('a', href=True):
#    print ilink['href']
