# Importing Libraries
import sqlite3


# Setting up SQLite3 Database framework
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Creating Tables
c.execute('''
CREATE TABLE tbl1(id INTEGER PRIMARY KEY ASC, name VARCHAR(50), number VARCHAR(250))
''')

c.execute('''
CREATE TABLE tbl1(id INTEGER PRIMARY KEY ASC, name VARCHAR(50), age VARCHAR(250), job VARCH
AR(250), hobbies VARCHAR(250))
''')


# Values to Insert into Tables
tbl1_insert_values = [
(1,'josh voss','8609314521'),
(2,'teresa cramer','6165236657'),
(3,'robert half','6160025453'),
(4,'kforce','6169967789'),
(5,'teksystems','6161145100')
]

tbl2_insert_values = [
(1,'josh voss','26','unemployed','basketball, datascience, meditation'),
(2,'teresa cramer','32','midwife','hiking, yoga, reading'),
(3,'magda','31','teaching assistant','reading, teaching')
]


# Inserting Table Values into Designed Tables
c.executemany('''
INSERT INTO tbl1(id, name, number)
VALUES (?, ?, ?)
''', tbl1_insert_values)

c.executemany('''
INSERT INTO tbl2(id, name, number)
VALUES (?, ?, ?)
''', tbl1_insert_values)


tbl_Column_Names = list(map(lambda x: x[0], c.execute('''SELECT * FROM tbl1''').description))
tbl1_Rows = c.execute('''SELECT * FROM tbl1''').fetchall()

tb2_Column_Names = list(map(lambda x: x[0], c.execute('''SELECT * FROM tbl2''').description))
tbl2_Rows = c.execute('''SELECT * FROM tbl2''').fetchall()


# Import PrettyTable Package
from prettytable import PrettyTable

y=PrettyTable()
y.padding_width = 1
y.add_column(tbl1_Column_Names[0],[ow[0] for row in tbl1_Rows])
y.add_column(tbl1_Column_Names[1],[row[1] for row in tbl1_Rows])
y.add_column(tbl1_Column_Names[2],[format(row[2],',d') for row in tbl1_Rows])
y.align[tbl1_Column_Names[1]]="l"
y.align[tbl1_Column_Names[2]]="r"

print(y)


####c.execute('''PRAGMA table_info(tbl1)''').fetchall()


