#You could use an import and single line code like this:

import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#Or define a function (Mbox) like so:
import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('Your title', 'Your text', 1)


#Note the styles are as follows:
##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No 
##  6 : Cancel | Try Again | Continue



#source: http://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
