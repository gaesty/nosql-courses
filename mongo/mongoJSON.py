import json
from pymongo import MongoClient
import pymongo

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélection de la base de données et de la collection
db = client.mydb
collection = db.mycollection

# with open("accounts.json", "r") as file:
#     data = json.load(file)
    
# result = collection.insert_many(data)

# print("Inserted data with the following IDs:", result.inserted_ids)

# index_name = "country_index"
# collection.create_index("country", name=index_name)

# city = "Spain"
# results = collection.find({"country": city})

# for result in results:
#     print(result)

# min_balance = 5
# results = collection.find({"numberrange": {"$gt": min_balance}})

# for result in results:
#     print(result)

# index_name = collection.create_index("email", unique=True)

pipeline = [
    {"$match": {"age": {"$gt": 25}}},
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(result)