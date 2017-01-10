import pandas as pd
import sqlite3


connection = sqlite3.connect('example.db')

dataframe = pd.read_sql_query("SELECT * FROM tbl1", connection)
df.to_csv('F:\\_\\-\\tbl1.csv', sep='\t')

read_csv = pd.read_csv('F:\\Data\\github\\ben519\\users.csv')
