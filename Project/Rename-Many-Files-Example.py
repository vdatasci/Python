import re
import os
for file in os.listdir('...\data\FileSortingFolder'):
    new_name = re.search('\#\d+', file).group(0) + ' ' + re.search('.*(?=\s\#)', file).group(0) + re.search('\.\w+$', file).group(0)
    os.rename(file, new_name)

# FileSortingFolder contains:
# Michael Jordan #23.txt
# Scottie Pippen #33.txt
# Dennis Rodman #91.txt

#This script runs
# and then renames the files as so:
# #91 Dennis Rodman.txt
# #23 Michael Jordan.txt
# #33 Scottie Pippen.txt
