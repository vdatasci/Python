#https://www.linkedin.com/vsearch/p?keywords=python&postalCode=49506&openAdvancedForm=true&locationType=I&countryCode=us&distance=50
#http://wiki.dreamrunner.org/public_html/Python/Python-Mechanize-Cheat-Sheet%20.html

from BeautifulSoup import BeautifulSoup
import mechanize
import requests
import re


url = 'http://www.linkedin.com'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open("https://www.linkedin.com/")
browser.form = list(browser.forms())[0]

for control in browser.form.controls:
    print control



username = browser.form.find_control("session_key").value
password = browser.form.find_control("session_password").value

username = ''
password = ''

browser.submit()

for resp in response.history:
        print resp.status_code, resp.url
        print response.url

browser.open('https://www.linkedin.com/')









url = 'https://www.linkedin.com/nhome/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

with open('P:\\TempFile.txt', 'w') as ff:
    ff.write(BeautifulSoup(html))


#Controls can be found by name like this
#control = br.form.find_control("controlname")

#for form in browser.forms():
#    print "Form name:", form.name
#    print form


#for prolink in soup.findAll('a', href=re.compile('^.*/profile/.*')):
#    print prolink.text
#    print playerlink['href']
#    print '\n'

#with open('P:\\TempFile.txt', 'w') as f:
#    f.write(a)
