import os
import fnmatch
import datetime
from tabulate import tabulate

path='P:\\'

configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in fnmatch.filter(files, '*.txt')]




v=[]
for file in configfiles:
    v.append((os.stat(file).st_size, os.path.basename(file), file))


print tabulate(v, headers=['Size:', 'FileName:', 'FullPath & FileName:'])
