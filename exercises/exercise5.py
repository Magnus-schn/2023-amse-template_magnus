import pandas as pd
import urllib.request
import zipfile
from sqlalchemy.types import Integer, String, Float

urllib.request.urlretrieve("https://gtfs.rhoenenergie-bus.de/GTFS.zip", "./exercises/exercise5.zip")
zip = zipfile.ZipFile("./exercises/exercise5.zip")
zip.extractall('./exercises')

Columns = ["stop_id","stop_name", "stop_lat", "stop_lon", "zone_id"]
Datatype = {"stop_id" : int, "stop_name" : str, "stop_lat" : float, "stop_lon" : float, "zone_id" : int}
df = pd.read_csv("./exercises/stops.txt",sep=',', decimal='.', index_col=False, usecols=Columns, dtype=Datatype, encoding='utf-8')

df = df[(df["zone_id"] == 2001)]

df = df[(df["stop_lat"] >= -90) & (df["stop_lat"] <= 90) & (df["stop_lon"] >= -90) & (df["stop_lon"] <= 90)]

#print(df)

Datatypesql = {"stop_id" : Integer, "stop_name" : String, "stop_lat" : Float, "stop_lon" : Float, "zone_id" : Integer}

df.to_sql('stops', 'sqlite:///./gtfs.sqlite', if_exists='replace', index=False, dtype=Datatypesql)