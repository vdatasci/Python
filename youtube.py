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
    linklist.append(BeautifulSoup(str(yt)).find(text=True).encode('utf-8').strip())
    print(BeautifulSoup(str(yt)).find(text=True).encode('utf-8').strip())

    
    
    
    
    
    
    
    
    
    

words = re.findall(r'\w+', str(linklist))
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)
word_counts


lwords = []
for key in sorted(word_counts.iterkeys()):
    lwords.append([key, word_counts[key]])



A = [‘letters’, ’letters’, ’letters\u2019’, ’vegetables’]
str(', '.join(A).encode('utf-8').strip())
