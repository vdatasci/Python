from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import sqlite3
import re



url= 'http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all'

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url)


response = requests.get(browser.geturl())
html = response.content
soup = BeautifulSoup(html)



from mechanize import Browser
br = Browser()
br.open("http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
br.select_form(name="tryitform")
sqlfield = br.form.find_control(id="textareaCodeSQL")
sqlfield.value = 'doodle'
response = br.submit()




print response.read()











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


headers_array = np.array(headers).reshape(1,-1)
rows_array = np.array(rows)
listsheet = np.vstack((headers_array, rows_array))
#listsheet

#Create Database Table
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE businesses
            (company VARCHAR(100),
            contact varchar(100),
            country varchar(100))''')
conn.commit()
conn.close()

#Insert Values into Database Table
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.executemany('''INSERT INTO businesses
            VALUES(?,?,?);''', rows_array.tolist())
conn.commit()
conn.close()

#Convert to CSV File
db = sqlite3.connect('example.db')
table = pd.read_sql_query("SELECT * from businesses", db)
table.to_csv('P:\TempSQL.csv', index=False)
