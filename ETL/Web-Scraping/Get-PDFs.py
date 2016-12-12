from BeautifulSoup import BeautifulSoup
import requests
import re

url= 'https://www.roberthalf.com/technology/salary-center-for-technology-professionals'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

pdflist = []
webpdfs = soup.findAll('a', {'href': re.compile('.*(pdf)')})
for pdf in webpdfs:
    pdflist.append(str(pdf['href']))

pdflist
