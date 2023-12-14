import pymongo
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, ObjectId):
      return str(o)
    return json.JSONEncoder.default(self, o)

class MongoService:
  def __init__(self):
    self.host = "mongodb://localhost:27017/"

  def connect(self):
    return pymongo.MongoClient(self.host)["Yelp"]
  
  def getBusinessByName(self, name: str, state: str | None, postal_code: str | None):
    connection = self.connect()
    collection = connection["Yelp Business"]
    if state is None:
      if postal_code is None:
        data = list(collection.find({ "name": name }))
      else:
        data = list(collection.find({ "name": name, "postal_code": postal_code }))
    else:
      if postal_code is None:
        data = list(collection.find({ "name": name, "state": state }))
      else:
        data = list(collection.find({ "name": name, "state": state, "postal_code": postal_code }))
    return json.loads(JSONEncoder().encode(data))
  
  def getBusinessById(self, business_id):
    connection = self.connect()
    collection = connection["Yelp Business"]
    data = collection.find_one({'business_id': business_id})
    return json.loads(JSONEncoder().encode(data))

  def getReviews(self, business_id):
    connection = self.connect()
    collection = connection["Yelp Review"]
    return list(collection.find({"business_id": business_id}))
  
  def getTrends(self, business_id):
    connection = self.connect()
    collection = connection["Yelp Review"]
    reviews = list(collection.find({"business_id": business_id}))
    count = len(reviews)
    avg_stars = sum(review["stars"] for review in reviews) / count if count > 0 else 0
    return {"business_id": business_id, "reviews_count": count, "avg_stars": avg_stars}
  
  def getCheckStars(self, business_id):
    connection = self.connect()
    collection = connection["Yelp Review"]
    reviews = list(collection.find({"business_id": business_id}))
    last_10_reviews = reviews[-10:]
    avg_stars = sum(review["stars"] for review in last_10_reviews) / len(last_10_reviews) if len(last_10_reviews) > 0 else 0
    return {"business_id": business_id, "reviews_count": len(last_10_reviews), "avg_stars": avg_stars}
    
    