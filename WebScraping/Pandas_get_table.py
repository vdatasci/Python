import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_logic_symbols'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

df = pd.read_html(str(soup), flavor="bs4")
df
