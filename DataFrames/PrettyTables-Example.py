from prettytable import PrettyTable
with open('P:\\Python\\Data\\randomdata.txt','r') as fp:
    reader = csv.DictReader(fp, dialect='excel-tab')
    ptable = PrettyTable(reader.fieldnames)
    for rowdict in reader:
        ptable.add_row([rowdict[fn] for fn in reader.fieldnames])
    print(ptable)
