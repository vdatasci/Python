from BeautifulSoup import BeautifulSoup
import numpy as np
import unicodedata
import requests
import re
import sqlite3
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import time


url = 'http://www.hotnewhiphop.com/'


response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)



li = soup.findAll('div', {'class': ['cover-title','dailySongChart-artist','dailySongChart-editor-review']})

lst = []
for l in li:
    lst.append(unicodedata.normalize('NFKD', l.text).encode('ascii','igonre'))


lst = np.resize(lst,(np.matrix(lst).size/3,3)).tolist()

for i in range(len(lst)/3):
    localtime = time.asctime( time.localtime(time.time()) )
    lst[i].insert(0,str(localtime))


conn = sqlite3.connect('HNHH.db')

df = pd.DataFrame(lst)
df.columns = ['Date', 'Song','Artist','Rating']

df.to_sql('Music', conn, if_exists='append')

pd.read_sql_query('SELECT * FROM Music', conn)
