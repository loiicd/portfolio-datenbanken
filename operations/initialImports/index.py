import pymongo
from initialImportMongo import inital_mongo_import

def index():
  userInput = input('Command: ')

  if userInput == 'import mongo':
    print('Execute Import Mongo...')
    inital_mongo_import()

  elif userInput == 'delete mongo':
    print('Execute Delete Mongo...')
    delete_data()

  elif userInput == 'exit':
    print('Exit...')
    exit()

  elif userInput == 'help':
    print('Commands: import mongo, delete mongo, exit')

  else:
    print('Invalid command')

def delete_data():
  client = pymongo.MongoClient("mongodb://localhost:27017/")
  db = client["Yelp"]
  collections = ["Yelp Business", "Yelp CheckIn", "Yelp Tip", "Yelp User", "Yelp Review"]
  
  for collection_name in collections:
    collection = db[collection_name]
    collection.delete_many({})
  
  print("All data deleted")

while True:
  index()