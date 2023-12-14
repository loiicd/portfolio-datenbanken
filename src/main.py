from fastapi import FastAPI, HTTPException
import redis
import os
import json
import pymysql.cursors

app = FastAPI()
print(f"Opening a new Redis connection on {os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}")
redis_conn = redis.StrictRedis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), decode_responses=True)
pubsub = redis_conn.pubsub()
pubsub.subscribe('review_alert')

# MySQL Connection Configuration
mysql_conn = pymysql.connect(
    host=os.getenv('MYSQL_HOST'),
    port=int(os.getenv('MYSQL_PORT')),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DATABASE'),
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

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
        redis_conn.publish('review_alert', f'Low ratings for {business_id}')

    return {"message": "Review added successfully"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
