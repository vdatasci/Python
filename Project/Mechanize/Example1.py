from mechanize import Browser

br = Browser()
br.open('http://www.city-data.com/')

br.find_link(text='CT')

req = br.click_link(text='CT')
br.open(req)

print br.geturl()

#print br.response().read()