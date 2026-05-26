from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["threat_intelligence"]

collection = db ["malicious_ips"]

for data  in collection.find():
     
    ip = data.get("ip", "Unknown")

    if ip.startswith ("192"):
        risk_score = "High"
    else:
        risk_score = "Medium"

    normalized_data  = {
       "ip": ip,
       "risk_score": risk_score
     }

    print (normalized_data) 

