import re
import sexmachine.detector as gender

txtdata = []
with open('P:\\Python\\babynames2014.txt') as f:
    for line in f:
        txtdata.append(str(line.rstrip('\n')))


alldata = []
alldata = ','.join(txtdata)
names_array = map(lambda x:str(x), alldata.split(','))


d = gender.Detector()
for name in names_array:
    if re.compile(r'\D').search(name) is not None:
        name + ': ' + str(d.get_gender(name))

