import os
import fnmatch
import datetime
from tabulate import tabulate

path='F:\\'

configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in fnmatch.filter(files, '*.txt')]


#basename = os.path.basename(file)

v=[]
for file in configfiles:
    v.append((os.stat(file).st_size, file))


with open('F:\TempFile.txt', 'w') as f:
    f.write(tabulate(v, headers=['Size:', 'File']))

    
    
