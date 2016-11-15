#div class='vk_c card-section'

import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.wunderground.com/weather-forecast/' + raw_input('ENTER ZIP CODE:  ')

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)


w = soup.findAll("div", {"id" : ["current"]})
w
