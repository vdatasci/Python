import sqlite3
import csv


conn = sqlite3.connect("db.sl3")
curs = conn.cursor()

reader = csv.reader(open('C:\\Users\\Linda\\Downloads\\Ginzberg.csv', 'r'), delimiter=',')

for row in reader:
    print row
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    curs.execute("INSERT INTO db (type, term, definition) VALUES (?, ?, ?);", to_db)


conn.commit()


