import pandas as pd
import sqlite3


connection = sqlite3.connect("db.sl3")
c = connection.cursor()

# csvfile_from_internet = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')

read_csv = pd.read_csv('F:\\Data\\github\\ben519\\users.csv')
read_csv.to_sql('test1', connection)

read_sql_query = pd.read_sql_query('''SELECT * FROM test1''', connection)


read_sql_query
read_csv

c.commit()
c.close()

