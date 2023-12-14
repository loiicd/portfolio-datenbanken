from fastapi import FastAPI, HTTPException
import redis
import os
import json
import mysql.connector

app = FastAPI()
print(f"opening a new redis on {os.getenv('HOST')}:{os.getenv('PORT')}")
r = redis.Redis(host=os.getenv('HOST'), port=os.getenv('PORT'))

try:
    # MySQL Connection Configuration
    mysql_conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        port=int(os.getenv('MYSQL_PORT')),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        charset='utf8mb4'
    )
    print("Connected to MySQL")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    raise

mysql_cursor = mysql_conn.cursor()

@app.get("/")
def read_root():
    return {"Hello": "WWI"}

@app.get("/hits")
def record_hits():
    r.incr("hits")
    return {"Hello": r.get("hits")}

def get_average_rating(business_id, n):
    with mysql_conn.cursor() as cursor:
        cursor.execute(f"SELECT stars FROM review WHERE business_id = '{business_id}' ORDER BY date DESC LIMIT {n}")
        ratings = [row['stars'] for row in cursor.fetchall()]

    if not ratings:
        return None  # Keine Bewertungen gefunden

    average_rating = sum(ratings) / len(ratings)
    return average_rating

@app.post("/reviews/{business_id}")
def add_review(business_id: str, review: dict):
    try:
        # Speichere die Bewertung in MySQL
        with mysql_conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO review (business_id, user_id, stars, useful, funny, cool, text, date) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (business_id, review['user_id'], review['stars'], review['useful'], review['funny'],
                review['cool'], review['text'], review['date'])
            )
        mysql_conn.commit()

        # Sende Benachrichtigung, wenn der Durchschnitt unter 2 ist
        average_rating = get_average_rating(business_id, 5)  # Durchschnitt der letzten 5 Bewertungen
        if average_rating is not None and average_rating < 2:
            r.publish('review_alert', f'Low ratings for {business_id}')

        return {"message": "Review added successfully"}
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
