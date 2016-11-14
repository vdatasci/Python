#This example uses the website API.GENDERIZE.IO to seperate baby names into categories.
#Depending on your gender preferences and political awareness, these gender assignments can be innacruate.
#From my understanding, these names are categorized by the most popular gender associated with each name.
#We cool?

import sexmachine.detector as gender

txtdata = []
#Replace the filepath and filename below with the destination of your data.
#In this example, we are using the babynames2014.txt file.
with open('P:\\Python\\babynames2014.txt') as f:
    for line in f:
        txtdata.append(str(line.rstrip('\n')))


alldata = ','.join(txtdata)
names_array = map(lambda x:str(x), alldata.split(','))

d = gender.Detector()
for name in names_array:
    if re.compile(r'\D').search(name) is not None:
        d.get_gender(name)
