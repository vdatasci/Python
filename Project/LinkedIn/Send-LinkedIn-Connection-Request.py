from BeautifulSoup import BeautifulSoup
import mechanize
import requests
import re


url = 'https://www.linkedin.com/vsearch/p?keywords=python&postalCode=49506&openAdvancedForm=true&locationType=I&countryCode=us&distance=50'
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



#Controls can be found by name like this
#control = br.form.find_control("controlname")




#for prolink in soup.findAll('a', href=re.compile('^.*/profile/.*')):
#    print prolink.text
#    print playerlink['href']
#    print '\n'

#with open('P:\\TempFile.txt', 'w') as f:
#    f.write(a)
