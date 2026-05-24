from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["threat_intelligence"]

collection = db["structured_threats"]

threat_data = {
    "ip": "192.168.1.10",
    "threat_type": "Malware",
    "risk_score": "High",
    "source": "OSINT Feed"
}

collection.insert_one(threat_data)

print ("Structured Threat Data Inserted")
