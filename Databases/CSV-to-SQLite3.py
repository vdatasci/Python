import sqlite3
import csv

reader = csv.reader(open('C:\\Users\\Linda\\Downloads\\Ginzberg.csv', 'r'), delimiter=',')

for row in reader:
    print row
