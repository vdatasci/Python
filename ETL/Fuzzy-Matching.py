from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re


choices = ["Chicago Bulls", "New York Knicks", "Brooklyn Nets", "LA Lakers", "Boston Celtics"]

### Tuples: ###
choices[0]
    'Chicago Bulls'
choices[1]
    'New York Knicks'
choices[2]
  'Brooklyn Nets'
choices[3]
    'LA Lakers'
choices[4]
    'Boston Celtics'
choices[-1]
    'Boston Celtics'
choices[-2]
    'LA Lakers'
###

### Fuzzy Match Processing: ###
process.extract("Brooklyn New York", choices, limit=2)
    [('Brooklyn Nets', 73), ('New York Knicks', 67)]

process.extractOne("Brooklyn New York", choices)
    ('Brooklyn Nets', 73)
    

fuzz.token_sort_ratio("This is a sentence", "A sentence is this")

fuzz.token_set_ratio("This is a sentence is this", "A sentence is this is a sentence")
