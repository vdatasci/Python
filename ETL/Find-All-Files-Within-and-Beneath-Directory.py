import os
import fnmatch

path='P:\\'

configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in fnmatch.filter(files, '*.txt')]

for file in configfiles:
    print(configfiles)
