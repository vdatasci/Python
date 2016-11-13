import re
import sqlite3
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def sql(statement, database, dataPath):
    import sqlite3
    dataPath = 'P:\Python\Database'
    db = sqlite3.connect(dataPath+'/'+database+'.db')
    sql = db.cursor().execute(statement)
    db.commit()
    db.close()

def show(statementPrint, database, dataPath)
    import sqlite3
    dataPath = 'P:\Python\Database'
    db = sqlite3.connect(dataPath+'/'+database+'.db')
    sql = db.cursor().execute(statement)
    sql.execute('SELECT * FROM person')
    print sql.fetchall()
    sql.execute(statementPrint)
    print sql.fetchall()
    conn.close()
    raw_input()



c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE address
          (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
           post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
           FOREIGN KEY(person_id) REFERENCES person(id))
          ''')

c.execute('''
          INSERT INTO person VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
          ''')

conn.commit()
conn.close()
raw_input()
