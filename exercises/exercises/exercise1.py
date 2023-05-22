import pandas as pd
from sqlalchemy import create_engine

# Definitions:
csv_url = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'

path = 'airports.sqlite'

table_name = 'airports'

df = pd.read_csv(csv_url, delimiter=";")

#test
#print(df)

sql = create_engine(f"sqlite:///{path}")

df.head(0).to_sql(table_name, sql, if_exists="replace", index=False)  

df.to_sql(table_name, sql, if_exists="replace", index=False)

sql.dispose()