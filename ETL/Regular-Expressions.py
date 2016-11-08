import re


rx = re.compile('p\@tt3rn')
result = rx.match(r'Match the word p@tt3rn in this string')
print(result.group(0))

strg = 'Find all letter i's in this string'
print(re.findall('i', strng)

strg = 'Split this string by the letter i'
print(re.split(r'a', strng)

