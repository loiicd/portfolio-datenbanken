import pymongo
import json
import pymongo

def connect():
  client = pymongo.MongoClient("mongodb://localhost:27017/")
  return client

def inital_mongo_import():
  db = connect()["Yelp"]
  insert_business(db)
  insert_checkin(db)
  insert_tip(db)
  insert_user(db)
  insert_review(db)
  print('Done')

def insert_business(db):
  print('Inserting Business')
  try:
    collection = db["Yelp Business"]
    data_list = []
    with open('./src/yelpData/yelp_academic_dataset_business.json') as f:
      for line in f:
        data = json.loads(line)
        data_list.append(data)
      collection.insert_many(data_list)
  except Exception as e:
    print('Error while inserting business', e)

def insert_checkin(db):
  print('Inserting Checkin')
  try:
    collection = db["Yelp CheckIn"]
    data_list = []
    with open('./src/yelpData/yelp_academic_dataset_checkin.json') as f:
      for line in f:
        data = json.loads(line)
        data_list.append(data)
      collection.insert_many(data_list)
  except Exception as e:
    print('Error while inserting checkin', e)

def insert_tip(db):
  print('Inserting Tip')
  try:
    collection = db["Yelp Tip"]
    data_list = []
    with open('./src/yelpData/yelp_academic_dataset_tip.json') as f:
      for line in f:
        data = json.loads(line)
        data_list.append(data)
      collection.insert_many(data_list)
  except Exception as e:
    print('Error while inserting tip', e)

def insert_user(db):
  print('Inserting User')
  try:
    collection = db["Yelp User"]
    with open('./src/yelpData/yelpUsers.yelpUsers.json', 'r') as file:
      data = json.load(file)
    for item in data:
      if '_id' in item and '$oid' in item['_id']:
        item['_id'] = {'oid': item['_id']['$oid']}
    collection.insert_many(data)
  except Exception as e:
    print('Error while inserting user:', e)

def insert_review(db):
  print('Inserting Review')
  try:
    collection = db["Yelp Review"]
    with open('./src/yelpData/yelpReviews.yelpReviews.json', 'r') as file:
      data = json.load(file)
    for item in data:
      if '_id' in item and '$oid' in item['_id']:
        item['_id'] = {'oid': item['_id']['$oid']}
    collection.insert_many(data)
  except Exception as e:
    print('Error while inserting review:', e)