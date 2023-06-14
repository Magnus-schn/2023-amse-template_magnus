import sqlite3
import pandas as pd

# Load Excel files
df1 = pd.read_excel('https://www.lba.de/SharedDocs/Downloads/DE/SBl/SBl3/Statistiken/Betrieb/Gefahrgutkontrollen.xlsx?__blob=publicationFile&v=5', engine='openpyxl')
df2 = pd.read_excel('https://www.lba.de/SharedDocs/Downloads/DE/SBl/SBl3/Statistiken/Betrieb/Gefahrgutzwischenfaelle.xlsx?__blob=publicationFile&v=5', engine='openpyxl')

# Rows to delete for each DataFrame
rows_to_delete1 = [0, 1, 2, 3, 4, 5, 6, 7]
rows_to_delete2 = [0, 1, 2, 3, 4, 5, 6, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

# Delete rows
df1.drop(rows_to_delete1, inplace=True)
df2.drop(rows_to_delete2, inplace=True)

#print(df1)
#print(df2)

# Modify column names
column_names1 = ['Year', 'German air carriers', 'Foreign air carriers','Handling Agents', 'German Airports and Aerodromes','Express Courier with own aeroplanes'] 
df1.columns = column_names1

column_names2 = ['Year','Incidents/Accidents','Accidents with injuries to persons','administrative offense proceedings','Applications for exemptions','Permissions for overflight','Approvals for the transport of Dangerous Goods for German air carriers']
df2.columns = column_names2

df1= df1.set_index('Year')
df2= df2.set_index('Year')

#print(df1)
#print(df2)

# Create a SQLite connection
conn = sqlite3.connect('./data/database.db')

# Write DataFrames to SQLite tables
df1.to_sql('Gefahrenkontrollen', conn, if_exists="replace")
df2.to_sql('Gefahrgutzwischenfaelle', conn, if_exists="replace")
