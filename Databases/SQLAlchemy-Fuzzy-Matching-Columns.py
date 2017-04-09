from sqlalchemy import create_engine
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#Creating an engine in memory
engine = create_engine('sqlite:///:memory:')

# URL of csv file, putting csv data into pandas dataframe
csv_url = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'
df = pd.read_csv(csv_url)

#Pushing df to sqlalchemy table
df.to_sql('table1', engine)

#querying the dataframe to make a new dataframe
qdf = pd.read_sql_query('''SELECT Transaction_date,Name,Last_Login FROM table1 WHERE Last_Login >= '2/9/09' ORDER BY Last_Login DESC''', engine)

#simple find of the value 'julie' in the column 'Name'
qdf[(qdf['Name'] == 'julie')]



lookups = ["julie","julia"]

choices = qdf.set_index("Transaction_date").Name.to_dict()

fuzzy_spots = [(lookup,) + item for lookup in lookups for item in process.extract(lookup, choices, limit=2)]
fdf = pd.DataFrame(fuzzy_spots, columns=["lookup", "matched", "score", "id"])
fdf
