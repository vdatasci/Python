import os
import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re


chromedriver = 'C:\Users\Linda\Desktop\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.linkedin.com/")

email = driver.find_element_by_class_name("login-email")
password = driver.find_element_by_class_name("login-password")

email.send_keys(str(raw_input('Email:  ')))
password.send_keys(str(raw_input('Password:  ')))

submit_button = driver.find_element_by_class_name('login-form')
submit_button.submit()



driver.get("https://www.linkedin.com/mynetwork/")

lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight


html = driver.page_source
soup = BeautifulSoup(html)

userlinks = []

for link in soup.findAll('a', {'href': re.compile('.*(/in/).*')}):
    userlinks.append(link['href'])


userlinks = sorted(list(set(userlinks)))

with open('F:\Python\Projects\LinkedIn\Data\LinkedIn_Network_URLs.txt', 'w') as f:
    for url in userlinks:
        f.write(url + '\n')



driver.get("https://www.linkedin.com" + userlinks[0])
html = driver.page_source
soup = BeautifulSoup(html)

name = str(soup.find('h1', {'class': re.compile('.*(pv-top-card-section__name).*')}).text).replace('\\n', '').replace('  ','').strip()
headline = str(soup.find('h2', {'class': re.compile('.*(pv-top-card-section__headline).*')}).text).replace('\\n', '').replace('  ','').strip()
company = str(soup.find('h3', {'class': re.compile('.*(pv-top-card-section__company).*')}).contents[0]).replace('\\n', '').replace('  ','').strip()
school = str(soup.find('h3', {'class': re.compile('.*(pv-top-card-section__school).*')}).contents[0]).replace('\\n', '').replace('  ','').strip()
degree = str(soup.find('p', {'class': re.compile('.*(pv-education-entity__secondary-title).*')}).parent.text).replace('\\n', '').replace('  ','').replace('\n', '').strip()
location = str(soup.find('h3', {'class': re.compile('.*(pv-top-card-section__location).*')}).text).replace('\\n', '').replace('  ','').strip()


#'https://www.linkedin.com' + soup.find('span', {'class': re.compile('.*(mn-person-info__name).*')}).parent['href']
#str(soup.find('span', {'class': re.compile('.*(mn-person-info__name).*')}).contents[0]).replace('\\n', '').replace('  ','').strip()
#str(soup.find('span', {'class': re.compile('.*(mn-person-info__occupation).*')}).contents[0]).replace('\\n', '').replace('  ','').strip()