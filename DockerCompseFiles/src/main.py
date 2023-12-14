from fastapi import FastAPI
import redis
import os
from pymongo import MongoClient

app = FastAPI()

# Verbindung zu Redis aufbauen
print(f"opening a new redis on {os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}")
r = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))

# Verbindung zu MongoDB aufbauen
mongo_client = MongoClient(
    host=os.getenv('MONGO_HOST', 'mongodb'),  # Verwende 'mongodb' als Standardwert, falls keine Umgebungsvariable festgelegt ist
    port=int(os.getenv('MONGO_PORT', 27017)),  # Verwende 27017 als Standardport, falls keine Umgebungsvariable festgelegt ist
)

# Verbindung zu MySQL aufbauen
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql',
    database='temperatur'
)

# MySQL-FastAPI-Pfad für Durchschnittstemperatur
@app.get("/temp/{region}")



# Route, um die vorhandenen Datenbanken in der MongoDB anzuzeigen
@app.get("/mongo_databases")
def get_mongo_databases():
    databases = mongo_client.list_database_names()
    return {"MongoDB Databases": databases}


# Route, um die MongoDB-Verbindung zu testen
@app.get("/mongo")
def test_mongo_connection():
    # Überprüfe die MongoDB-Verbindung und gib Informationen zurück
    return {"MongoDB Connection": str(mongo_client.server_info())}

@app.get("/1")
def read_root():
    return {"Hello": "WWI"}

@app.get("/hits")
def record_hits():
    r.incr("hits")
    return {"Hello": r.get("hits")}
