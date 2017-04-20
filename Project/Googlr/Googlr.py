from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import mechanize
import requests
import urllib2
import re


url = 'https://www.google.com'
response = requests.get(str(url))
html = response.content
soup = BeautifulSoup(html)
