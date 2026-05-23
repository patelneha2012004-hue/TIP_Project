import requests

from db_connect import collection
from ioc_validator import validate_ip

url = "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"

response = requests.get(url)

lines = response.text.split("\n")

for line in lines:

    if line.startswith("#") or line.strip() == "":
        continue

    ip = line.strip()

    if validate_ip(ip):

        data = {
            "ip": ip,
            "source": "Abuse.ch",
            "risk": "high"
        }

        collection.insert_one(data)

        print(f"[+] Valid IOC Inserted: {ip}")

    else:
        print(f"[-] Invalid IOC Skipped: {ip}")

print("Done")
