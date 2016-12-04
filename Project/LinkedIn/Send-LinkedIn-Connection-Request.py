from BeautifulSoup import BeautifulSoup
import requests
import re


url = 'https://www.linkedin.com/vsearch/p?keywords=python&postalCode=49506&openAdvancedForm=true&locationType=I&countryCode=us&distance=50'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)


for prolink in soup.findAll('a', href=re.compile('^.*/profile/.*')):
    print prolink.text
    print playerlink['href']
    print '\n'

#with open('P:\\TempFile.txt', 'w') as f:
    #f.write(a)
