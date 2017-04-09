import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

csv_url = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'
df = pd.read_csv(csv_url)

df.to_sql('table1', engine)
