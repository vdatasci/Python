#This example uses the website API.GENDERIZE.IO to seperate baby names into categories.
#Depending on your gender preferences and political awareness, these gender assignments can be innacruate.
#From my understanding, these names are categorized by the most popular gender associated with each name.
#We cool?

import re
import urllib
import requests
from BeautifulSoup import BeautifulSoup

txtdata = []
#Replace the filepath and filename below with the destination of your data.
#In this example, we are using the babynames2014.txt file.
with open('P:\\Python\\babynames2014.txt') as f:
    for line in f:
        txtdata.append(str(line.rstrip('\n')))


alldata = ','.join(txtdata)
names_array = map(lambda x:str(x), alldata.split(','))


for name in names_array:
    if re.compile(r'\D').search(name) is not None:
		url = 'https://api.genderize.io/?name=' + name
		response = requests.get(url)
		html = response.content
		soup = BeautifulSoup(html)
    #Replace the filepath and filename below with your destination and filename.
    #In this example, we are saving the data to a file that happens to be called 'TempFile' but is not a temporary file.
		with open('P:\Python\TempFile.txt','a') as f:
			f.write(name + ' is a ')
			f.write(re.search('((?<=\"gender":\")|(?<=\"gender":))\w+', str(soup.contents)).group(0))
			f.write('. ')
			f.write('\n')

