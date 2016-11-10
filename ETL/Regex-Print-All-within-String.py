import re;

s = "ABC12DEF3G56HIJ7"
pattern = re.compile(r'([A-Z]+)([0-9]+)');

for (letters, numbers) in re.findall(pattern, s):
    print numbers, '*', letters

#12 * ABC
#3 * DEF
#56 * G
#7 * HIJ
