#div class='vk_c card-section'

import requests
from BeautifulSoup import BeautifulSoup
import re


url = 'https://weather.com/weather/hourbyhour/l/Mansfield+Center+CT+06250'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)


w = soup.find("td", {"class" : ["temp"]})
w.text

weather = re.search('\d+', w.text).group(0)

print weather
