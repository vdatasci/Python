from mechanize import Browser
import webbrowser

br = Browser()
br.open('http://www.city-data.com/')

br.find_link(text='CT')
req = br.click_link(text='CT')
br.open(req)
print br.geturl()
clickedurl = br.geturl()



#br.open(clickedurl).read()
#webbrowser.open(clickedurl,new=1)

#browser.select_form(nr = 0)
f = br.retrieve('http://pics3.city-data.com/images/data-stats-new.png')[0]
print f
fh = open(f)



#print br.response().read()
