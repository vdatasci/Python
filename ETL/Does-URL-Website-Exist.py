from urllib2 import urlopen
code = urlopen("http://example.com/").code
if (code / 100 >= 4):
   print "Nothing there."

code
