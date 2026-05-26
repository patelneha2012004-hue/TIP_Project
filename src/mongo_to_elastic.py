
from pymongo import MongoClient

print("MongoDB Connected")

client = MongoClient("mongodb://localhost:27017/")

db = client["threat_intelligence"]

collection = db["structured_threats"]

for data in collection.find():

    print(data)

print ("Threat Data Read Successfully")
