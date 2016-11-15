#div class='vk_c card-section'

import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.wunderground.com/weather-forecast/06268'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)


w = soup.find("div", {"id" : ["current"]})
w.text

f = soup.find("span", {"class" : ["wx-value"]})
f.text

