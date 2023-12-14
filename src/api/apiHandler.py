from fastapi import FastAPI
from mySQLService import MySQLService

app = FastAPI()
mySQLService = MySQLService()

@app.get("/")
def read_root():
  return 'Hello'

@app.get('/statistics/{business_id}')
def getStatistics(business_id: str):
  return mySQLService.getStatistics(business_id)
