from BeautifulSoup import BeautifulSoup
import mechanize
import requests
import re


browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open("http://services.runescape.com/m=itemdb_oldschool/top100?list=0")


for form in browser.forms():
    print "Form name:", form.name
    print form


browser.form = list(browser.forms())[0]


for control in browser.form.controls:
    print control
    print '\n'
    print control.type


