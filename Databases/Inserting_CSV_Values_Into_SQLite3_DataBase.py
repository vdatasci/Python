# Importing Libraries
import sqlite3
import csv
Import pandas as pd


# Building SQLite3 Database Framework
connection = sqlite3.connect('new.db')
c = connection.cursor()

# Building SQLite3 Table
c.execute('''
CREATE TABLE table1(id INTEGER PRIMARY KEY ASC, first_name VARCHAR(50), last_name VARCHAR(50))
''')


# Building list tuple from csv file
with open('F:\\Data\\Samples\\names.csv') as f:
    inserting_csv_values = map(tuple, csv.reader(f))


# Inserting CSV Values into Table
c.executemany('''
INSERT INTO table1(id, name, number)
VALUES (?, ?, ?)
''', inserting_csv_values)


# Printing Pandas SQL Query and Saving Query as HTML and CSV
df = pd.read_sql_query("SELECT * FROM table1", connection)
print(df)

print(df[df['first_name'].str.contains(u'(josh|(.*(a).*))')])

df.to_html('F:\\_\\-\\sqlite3_query_pandas_to_html.html')
df.to_csv('F:\\_\\-\\sqlite3)query_pandas_to_csv.csv')
