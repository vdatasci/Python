from urllib2 import urlopen
code = urlopen("http://example.com/").code
if (code / 100 >= 4):
   print "Nothing there."

code





#from urllib2 import urlopen
#url = 'http://uconn.edu/yo'
#f = urllib.urlopen(url)
#if f.code==200:
#    fxst = 'exists'
