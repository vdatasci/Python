from urllib2 import urlopen
code = urlopen("http://example.com/").code
if (code / 100 >= 4):
   print "Nothing there."
code


def checkwww(url):
   if ((urlopen(url).code / 100) >= 4):
      print "Nothing there."
   else
      print "Exists."




#from urllib2 import urlopen
#url = 'http://uconn.edu/yo'
#f = urllib.urlopen(url)
#if f.code==200:
#    fxst = 'exists'


#Grab all text from webpage
   #http://savkar.math.uconn.edu/files/dfdf
   #http://web.stanford.edu/class/sdfsf
      #fuzzy regex to see if page exists: (Not Found)|(404 Error)
