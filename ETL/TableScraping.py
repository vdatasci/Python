from BeautifulSoup import BeautifulSoup
import mechanize
import requests
import re


url= 'http://www.w3schools.com/html/html_tables.asp'
url2 = 'http://services.runescape.com/m=itemdb_oldschool/top100?list=0'


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


del rows[0]


with open('P:\TempFile.txt', 'w') as f:
    f.write(str(', '.join(headers)))


with open("P:\TempFile.txt", "a") as f:
    for r in rows:
        f.write(str(', '.join(r)) + '\n')



import numpy as np

headers_array = np.array(headers).reshape(1,-1)
rows_array = np.array(rows)
listsheet = np.vstack((headers_array, rows_array))

listsheet









import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE businesses
            (company VARCHAR(100),
            contact varchar(100),
            country varchar(100))''')
conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('SELECT * FROM businesses')
print c.fetchall()
conn.close()










import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

c.executemany('''INSERT INTO businesses
            VALUES(?,?,?);''', rows_array.tolist())
conn.commit()
conn.close()



import pandas as pd
db = sqlite3.connect('example.db')
table = pd.read_sql_query("SELECT * from businesses", db)
table.to_csv('P:\TempSQL.csv', index_label='index')
