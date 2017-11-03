#Dependencies: FuzzyWuzzy, Fuzzy (Soundex), RE, PyDictionary, PyPhonetics, Phonetics

import fuzzy
import fuzzywuzzy
from fuzzywuzzy import process
import re
import PyDictionary
import PyPhonetics
import phonetics




l = ['comics', 'muskegan', 'bob', 'downtown', 'court', 'sued', 'spilled ink']
for word in l:
    process.extract(word, l, limit=len(l))
