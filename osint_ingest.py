import requests
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["threat_intelligence"]

collection = db["malicious_ips"]

url= "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"

response = requests.get(url)

lines = response.text.split("\n")

for line in lines:
 
  if line.startswith("#") or line.strip() == "":
      continue
 
  ip = line.strip()

  data = {
    "ip":ip,
    "source":"Abuse.ch",
    "risk":"high"
   }

  collection.insert_one(data)

  print (ip)

print ("Done")
