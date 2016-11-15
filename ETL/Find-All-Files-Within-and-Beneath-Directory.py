import os
import fnmatch
from tabulate import tabulate

path='P:\\'

configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in fnmatch.filter(files, '*.txt')]


print tabulate([['Alice', 24], ['Bob', 19]], headers=['Size', 'FileName', 'Date Created'])

v = []
for file in configfiles:
    v = os.stat(file).st_size, '\t', file, '\t', os.stat(file).st_ctime
    #print os.stat(file).st_size, '\t', file, '\t', os.stat(file).st_ctime
