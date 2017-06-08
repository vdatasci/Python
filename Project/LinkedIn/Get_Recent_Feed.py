import os
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import unicodedata
import pandas as pd

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

#driver.get("https://www.linkedin.com/feed/")
#html = driver.page_source
#soup = BeautifulSoup(html)

driver.current_url

for i in range(100):
    driver.find_element_by_tag_name('body').send_keys(webdriver.common.keys.Keys.END)


html = driver.page_source
soup = BeautifulSoup(html)

posts = []
for post in soup.findAll('article', {'class': re.compile('.*(feed-s-update).*')}):
    posts.append(post)


postslist = []

for p in range(len(posts)):
    try:
        name = (BeautifulSoup(str(posts[p]), "lxml").findAll('a', {'class': re.compile('.*(meta__profile-link).*')})[0].text).split('\n')[1]
        title = (BeautifulSoup(str(posts[p]), "lxml").findAll('a', {'class': re.compile('.*(meta__profile-link).*')})[0].text).split('\n')[3]
        link = 'http://www.linkedin.com' + str(BeautifulSoup(str(posts[p]), "lxml").findAll('a', {'class': re.compile('.*(meta__profile-link).*')})[0]['href'])
        content = BeautifulSoup(str(posts[p]), "lxml").findAll('p', {'class': re.compile('.*(feed-s-main-content ember-view).*')})[0].text
        postslist.append([name, title, link, content])
    except IndexError:
        pass

q

df = pd.DataFrame(postslist)

pd.options.display.max_colwidth = 200

df[df[3].str.contains(u'Python|SQL|sql|python|developer|Developer|Analyst|analyst')][2]
df[df[3].str.contains(u'Python|SQL|sql|python|developer|Developer|Analyst|analyst')][3]



raw_list_posts = list(df[3])

#regex search linkedin posts for 'job':
filter(re.compile('.*(job).*').match, list(df[3]).replace('\n', '').replace('\t', ''))
#Index of that post (make into choosable list):
postindex = list(df[3]).index(str(filter(re.compile('.*(hiring).*').match, list(df[3]))[1]))
df[0][int(postindex)]


###
BeautifulSoup(str(posts[0])).findAll('a', {'class': re.compile('.*(meta__profile-link).*')})[0].text
BeautifulSoup(str(posts[0])).findAll('a', {'class': re.compile('.*(meta__profile-link).*')})[0]['href']
###
#BeautifulSoup(str(posts[0])).findAll('p', {'class': re.compile('.*(feed-s-main-content ember-view).*')})
BeautifulSoup(str(posts[0])).findAll('p', {'class': re.compile('.*(feed-s-main-content ember-view).*')})[0].text
###






posts[0].text
posts[0].findAll()[0].text

postzero_tagnames = [tag.name for tag in BeautifulSoup(posts[0], "html.parser").findAll()]


tag_names = [tag.name for tag in soup.findAll()]

tagtexts = [tag.text for tag in BeautifulSoup(str(posts), "html.parser")]
tagnames = [tag.name for tag in BeautifulSoup(str(posts), "html.parser")]



	#work on this
childtags = []
for tag in BeautifulSoup(str(posts[0])):
    childtags.append(unicodedata.normalize('NFKD', tag.text).encode('ascii', 'ignore'))

childtags2text = []
childtags2name = []
for tag2 in BeautifulSoup(str(posts[0])):
    childtags2text = (unicodedata.normalize('NFKD', tag2.text).encode('ascii', 'ignore')).split('\n')
    childtags2name.append(tag2.name)



soupfind = [x for x in soup.find('article', {'class': re.compile('.*(feed-s-update).*')})]
soupfind.pop(0)
soupfind
