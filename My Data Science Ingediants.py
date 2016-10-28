import requests,BeautifulSoup,bs4,sqlalchemy,numpy,pandas,pygal,matplotlib,pylab,flask,django,selenium,scipy,pyopt,adodbapi,Tkinter,math,xlrd,statistics,geopy,fuzzywuzzy,praw
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import pandas as pd
import numpy as np
#import ctypes  # An included library with Python install.
#ctypes.windll.user32.MessageBoxA(0, "  " + e, "Your title", 1)
import easygui
###

choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
e = str(process.extract("new york jets", choices, limit=2))
#print process.extract("new york jets", choices, limit=2)
easygui.msgbox(e, title="simple gui")



