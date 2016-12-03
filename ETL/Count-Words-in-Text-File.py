import re
from collections import Counter

with open('P:\commonwords.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)
word_counts
