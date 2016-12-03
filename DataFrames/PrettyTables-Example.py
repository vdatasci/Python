from prettytable import PrettyTable
import csv

with open('P:\\Python\\Data\\randomdata.txt','r') as f:
    reader = csv.DictReader(f, dialect='excel-tab')
    ptable = PrettyTable(reader.fieldnames)
    for rowdict in reader:
        ptable.add_row([rowdict[fn] for fn in reader.fieldnames])
    print(ptable)
