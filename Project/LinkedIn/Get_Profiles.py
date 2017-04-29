import os
import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import numpy as np
import unicodedata


chromedriver = 'C:\Users\Linda\Desktop\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.linkedin.com/")

email = driver.find_element_by_class_name("login-email")
password = driver.find_element_by_class_name("login-password")

email.send_keys('JoshVoss90@Outlook.com')
password.send_keys('Jobpassword1!')

submit_button = driver.find_element_by_class_name('login-form')
submit_button.submit()


with open('F:\Python\Projects\LinkedIn\Data\LinkedIn_Network_URLs.txt', 'r') as f:
    contents = f.readlines()


userlinks = ['https://www.linkedin.com' + x.strip() for x in contents]


for z in range(len(userlinks)):
    driver.get(userlinks[z])
    html = driver.page_source
    soup = BeautifulSoup(html)
    
    try:
        name = soup.find('h1', {'class': re.compile('.*(pv-top-card-section__name).*')}).text
    except AttributeError:
        pass
    try:
        headline = soup.find('h2', {'class': re.compile('.*(pv-top-card-section__headline).*')}).text
    except AttributeError:
        pass
    try:
        company = soup.find('h3', {'class': re.compile('.*(pv-top-card-section__company).*')}).contents[0]
    except AttributeError:
        pass
    try:
        school = soup.find('h3', {'class': re.compile('.*(pv-top-card-section__school).*')}).contents[0]
    except AttributeError:
        pass
    try:
        degree = soup.find('p', {'class': re.compile('.*(pv-education-entity__secondary-title).*')}).parent.text
    except AttributeError:
        pass
    try:
        location = soup.find('h3', {'class': re.compile('.*(pv-top-card-section__location).*')}).text
    except AttributeError:
        pass
    
    	
    with open('F:\Python\Projects\LinkedIn\Data\LinkedIn_Network_Info.txt', 'a') as f:
        f.write(str(unicodedata.normalize('NFKD', name).encode('ascii','replace')).replace('\\n', ' ~ ').replace('  ','').replace('\n', ' ~ ').strip())
        f.write(str(', '))
        f.write(str(unicodedata.normalize('NFKD', headline).encode('ascii','replace')).replace('\\n', ' ~ ').replace('  ','').replace('\n', ' ~ ').strip())
        f.write(str(', '))
        f.write(str(unicodedata.normalize('NFKD', company).encode('ascii','replace')).replace('\\n', ' ~ ').replace('  ','').replace('\n', ' ~ ').strip())
        f.write(str(', '))
        f.write(str(unicodedata.normalize('NFKD', school).encode('ascii','replace')).replace('\\n', ' ~ ').replace('  ','').replace('\n', ' ~ ').strip())
        f.write(str(', '))
        f.write(str(unicodedata.normalize('NFKD', degree).encode('ascii','replace')).replace('\\n', ' ~ ').replace('  ','').replace('\n', ' ~ ').strip())
        f.write(str(', '))
        f.write(str(unicodedata.normalize('NFKD', location).encode('ascii','replace')).replace('\\n', ' ~ ').replace('  ','').replace('\n', ' ~ ').strip())
        f.write(str('\n'))
        f.write(str('\n'))


#.replace('\\n', '').replace('  ','').encode('utf-8').strip()

#'https://www.linkedin.com' + soup.find('span', {'class': re.compile('.*(mn-person-info__name).*')}).parent['href']
#str(soup.find('span', {'class': re.compile('.*(mn-person-info__name).*')}).contents[0]).replace('\\n', '').replace('  ','').strip()
#str(soup.find('span', {'class': re.compile('.*(mn-person-info__occupation).*')}).contents[0]).replace('\\n', '').replace('  ','').strip()
