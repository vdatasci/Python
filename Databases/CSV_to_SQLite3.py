import pandas as pd
import sqlite3

csvfile_name = pd.read_csv('F:\\Data\\github\\ben519\\users.csv')
# csvfile_name_from_internet = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')

connection = sqlite3.connect("db.sl3")
c = conn.cursor()

read_csv = pd.read_csv('F:\\Data\\github\\ben519\\users.csv')
read_csv.to_sql('test1', connection)

sql_query = raw_input('Input SQL Query:  ')
read_sql_query = pd.read_sql_query(sql_query, connection)


read_sql_query
read_csv

