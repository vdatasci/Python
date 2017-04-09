import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

csv_url = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'
df = pd.read_csv(csv_url)

df.to_sql('table1', engine)

qdf = pd.read_sql_query('''SELECT Transaction_date,Name,Last_Login FROM table1 WHERE Last_Login >= '2/9/09' ORDER BY Last_Login DESC''', engine)

qdf[(qdf['Name'] == 'julie')]



lookups = ["julie","julia"]

choices = qdf.set_index("Transaction_date").Name.to_dict()

res = [(lookup,) + item for lookup in lookups for item in process.extract(lookup, choices, limit=2)]
rdf = pd.DataFrame(res, columns=["lookup", "matched", "score", "id"])
rdf
