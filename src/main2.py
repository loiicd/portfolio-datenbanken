import pymongo
import mysql.connector
from datetime import datetime

# MongoDB-Verbindung herstellen
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["Yelp"]
yelp_checkin_collection = mongo_db["Yelp CheckIn"]

# MySQL-Verbindung herstellen
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="Yelp",
    port=3306
)
mysql_cursor = mysql_connection.cursor()

# MySQL-Tabelle "CheckIn" erstellen mit zwei getrennten Spalten für Datum und Zeit
mysql_cursor.execute("""
    CREATE TABLE IF NOT EXISTS CheckIn (
        id INT AUTO_INCREMENT PRIMARY KEY,
        business_id VARCHAR(255),
        checkin_date DATE,
        checkin_time TIME,
        FOREIGN KEY (business_id) REFERENCES Business(business_id)
    )
""")

# Daten von Yelp CheckIn abrufen und in MySQL einfügen (nur wenn business_id in Business-Tabelle vorhanden ist) mit Batch-Funktionalität
checkin_data = []
batch_size = 1000  # Beispiel: Batch-Größe von 1000 Datensätzen

for document in yelp_checkin_collection.find():
    business_id = document.get("business_id", "")

    # Prüfen, ob die business_id in der Business-Tabelle vorhanden ist
    mysql_cursor.execute("SELECT business_id FROM Business WHERE business_id = %s", (business_id,))
    result = mysql_cursor.fetchone()

    if result:
        date_time_pairs = document.get("date", "").split(", ")
        for date_time_str in date_time_pairs:
            date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
            checkin_date = date_time.strftime("%Y-%m-%d")
            checkin_time = date_time.strftime("%H:%M:%S")
            checkin_data.append((business_id, checkin_date, checkin_time))

            # Prüfe, ob die Batch-Größe erreicht ist, und führe einen Bulk Insert durch
            if len(checkin_data) >= batch_size:
                mysql_cursor.executemany(
                    "INSERT INTO CheckInNeu (business_id, checkin_date, checkin_time) VALUES (%s, %s, %s)",
                    checkin_data
                )

                # Leere die Liste für die nächste Batch-Gruppe
                checkin_data = []

# Führe einen letzten Bulk Insert für die verbleibenden Datensätze durch
if checkin_data:
    mysql_cursor.executemany(
        "INSERT INTO CheckInNeu (business_id, checkin_date, checkin_time) VALUES (%s, %s, %s)",
        checkin_data
    )

# Änderungen in MySQL commiten und Verbindungen schließen
mysql_connection.commit()
mysql_cursor.close()
mysql_connection.close()
