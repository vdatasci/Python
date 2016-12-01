from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re


choices = ['Hit', 'Stay', 'Double Down']

say = raw_input("Hit? Stay? Double Down? ")

m = re.search('(?<=\(\').*(?=\'\,)', str(process.extract(say, choices, limit=1))).group(0)
n = choices.index(re.search('(?<=\(\').*(?=\'\,)', str(process.extract(say, choices, limit=1))).group(0))

print m
print n


raw_input()
#turn m into a linear search
