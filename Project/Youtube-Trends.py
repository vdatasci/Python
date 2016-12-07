from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import sqlite3
import re


url= 'https://www.youtube.com/feed/trending'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)


linklist = []
ytitles = soup.findAll('a', {'href': re.compile('.*(watch\?v).*')})
for yt in ytitles:
        linklist.append(str(yt['href'])+str(', '))


vtitles = []
for v in vlist:
        urlgo= 'http://www.youtube.com/watch?v=' + re.search('(?<=\=).*', str(v)).group()
        response = requests.get(urlgo)
        html = response.content
        soup = BeautifulSoup(html)
        vtitles.append(str((soup.findAll('title'))).replace('[<title>','').replace('</title>]',''))







from collections import Counter
words = re.findall(r'\w+', str(vtitles))
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)
word_counts








from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
words = re.findall(r'\w+', str(vtitles))
cap_words = [word.upper() for word in words]
labels, values = zip(*Counter(cap_words).most_common())
indexes = np.arange(len(labels[:5]))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()
