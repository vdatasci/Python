from prettytable import PrettyTable
import csv
import requests

data = requests.get('https://raw.githubusercontent.com/vdatasci/Python/master/DataFrames/data/randomdata.txt').content

with open(data,'r') as f:
    reader = csv.DictReader(f, dialect='excel-tab')
    ptable = PrettyTable(reader.fieldnames)
    for rowdict in reader:
        ptable.add_row([rowdict[fn] for fn in reader.fieldnames])
    print(ptable)
