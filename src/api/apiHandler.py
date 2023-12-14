from fastapi import FastAPI
from mongoService import MongoService

app = FastAPI()
mongoService = MongoService()

@app.get('/business/name/{name}')
def getBusinessByName(name: str, state: str | None = None, postal_code: str | None = None):
  return mongoService.getBusinessByName(name, state, postal_code)

@app.get('/business/{business_id}')
def getBusinesses(business_id):
  return mongoService.getBusinessById(business_id)

@app.get('/reviews/{business_id}')
def getReviews(business_id):
  return mongoService.getReviews(business_id)

@app.get('/reviews/trends/{business_id}')
def getTrends(business_id):
  return mongoService.getTrends(business_id)

@app.get('/reviews/checkstars/{business_id}')
def getCheckStars(business_id):
  return mongoService.getCheckStars(business_id)