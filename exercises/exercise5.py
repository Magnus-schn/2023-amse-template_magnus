import os
import pandas as pd
import urllib.request
import zipfile
from sqlalchemy.types import Integer, String, Float

urllib.request.urlretrieve("https://gtfs.rhoenenergie-bus.de/GTFS.zip", "./exercises/Zip.zip")
zip = zipfile.ZipFile("./exercises/Zip.zip")
zip.extractall('./exercises')

Columns = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
DataType = {"stop_id": int, "stop_name": str, "stop_lat": float, "stop_lon": float, "zone_id": int}
df = pd.read_csv("./exercises/stops.txt", sep=',', decimal='.', index_col=False, usecols=Columns, dtype=DataType, encoding='utf-8')

df = df[(df["zone_id"] == 2001)]

df = df[(df["stop_lat"] >= -90) & (df["stop_lat"] <= 90) & (df["stop_lon"] >= -90) & (df["stop_lon"] <= 90)]

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "gtfs.sqlite")

DataTypessql= {"stop_id": Integer, "stop_name": String, "stop_lat": Float, "stop_lon": Float, "zone_id": Integer}
df.to_sql('stops', f'sqlite:///{db_path}', if_exists='replace', index=False, dtype=DataTypessql)