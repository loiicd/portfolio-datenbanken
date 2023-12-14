from fastapi import FastAPI
import redis
import os

app = FastAPI()
print(f"opening a new redis on {os.getenv('HOST')}:{os.getenv('PORT')}")
r = redis.Redis(host=os.getenv('HOST'), port=os.getenv('PORT'))
# r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"Hello": "WWI"}

@app.get("/hits")
def record_hits():
    r.incr("hits")
    return {"Hello": r.get("hits")}
