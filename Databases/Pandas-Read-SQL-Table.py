import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

df = pd.DataFrame({'A': [1,2,3], 'B': ['a', 'b', 'c']})

df.to_sql('db_table', engine, index=False)

pd.read_sql_table('db_table', engine)
