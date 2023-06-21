import pandas as pd
import re

from sqlalchemy import create_engine

# Define the source file URL and target database

data_url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'

database_name = 'cars.sqlite'


# Read the CSV file into a DataFrame, skipping the metadata lines
new_column_names = ["date", "CIN", "name", "petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]
columns_for_sql = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]


df = pd.read_csv(data_url, skiprows=6, skipfooter=4, encoding='latin1', delimiter= ";", usecols=columns_for_sql)

df.columns = new_column_names
# df.set_axis(new_column_names, axis=1, inplace=True)


# Validate and clean the data

df['CIN'] = df['CIN'].astype(str).str[:5].str.pad(width=5, side='right', fillchar='0')   # CIN validation

df = df[df[['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']].apply(pd.to_numeric, errors='coerce').gt(0).all(axis=1)]  # Positive integer validation

data_types = {
    "date" : str,
    "CIN" : str,
    "name" : str,
    "diesel": int,
    "electro": int,
    "gas": int,
    "hybrid": int,
    "plugInHybrid": int,
    "others": int,
    "petrol": int
}    
df = df.astype(data_types)
# Create a SQLite database engine and write the DataFrame to a table

engine = create_engine(f'sqlite:///{database_name}')

df.to_sql('cars', engine, if_exists='replace', index=False)