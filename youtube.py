from BeautifulSoup import BeautifulSoup
from collections import Counter
import requests
import urllib


url = 'https://www.youtube.com/feed/trending'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

linklist = []
ytitles = soup.findAll('div', {'class': 'yt-lockup-content'})
for yt in ytitles:
    linklist.append(BeautifulSoup(str(yt)).find(text=True))

linklist


words = re.findall(r'\w+', str(linklist))
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)
word_counts
