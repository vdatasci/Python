from prettytable import PrettyTable
import csv
import urllib2

data = urllib2.urlopen('https://raw.githubusercontent.com/vdatasci/Python/master/DataFrames/data/randomdata.txt')

with open(data,'r') as f:
    reader = csv.DictReader(f, dialect='excel-tab')
    ptable = PrettyTable(reader.fieldnames)
    for rowdict in reader:
        ptable.add_row([rowdict[fn] for fn in reader.fieldnames])
    print(ptable)
