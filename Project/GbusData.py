import requests
from BeautifulSoup import BeautifulSoup


url = 'https://www.google.com/search?tbm=lcl&ei=OoL4WcTZPIiT0gKGjKTIBw&q=In+the+Image+Clothing+Center&oq=In+the+Image+Clothing+Center&gs_l=psy-ab.3...0.0.0.5259.0.0.0.0.0.0.0.0..0.0....0...1..64.psy-ab..0.0.0....0.luBDMKDV08o#rlfi=hd:;si:8178925334166259136;mv:!1m3!1d328.07309953525464!2d-85.6669464!3d42.9302853!2m3!1f0!2f0!3f0!3m2!1i465!2i690!4f13.1'


response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

soup.findAll('div')
