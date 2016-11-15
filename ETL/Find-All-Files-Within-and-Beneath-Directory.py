import os
import fnmatch

path='P:\\'

configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in fnmatch.filter(files, '*.txt')]


print 'Size:', '\t', 'FileName:', '\t', 'Date Created:'
for file in configfiles:
    print os.stat(file).st_size, '\t', file, '\t', os.stat(file).st_ctime
