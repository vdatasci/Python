from BeautifulSoup import BeautifulSoup
import numpy as np
import unicodedata
import requests
import re
import sqlite3
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


url = 'http://www.hotnewhiphop.com/'


response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)



li = soup.findAll('div', {'class': ['cover-title','dailySongChart-artist','dailySongChart-editor-review']})

lst = []
for l in li:
    lst.append(unicodedata.normalize('NFKD', l.text).encode('ascii','igonre'))


lst = np.resize(lst,(np.matrix(lst).size/3,3)).tolist()


conn = sqlite3.connect('example.db')

df = pd.DataFrame(lst)
df.columns = ['Song','Artist','Rating']

df.to_sql('Music', conn, if_exists='append')

