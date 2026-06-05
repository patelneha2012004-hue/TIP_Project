threat_feeds = [
    {"ioc": "malicious-domain.com", "category": "Malware"},
    {"ioc": "phishing-site.net", "category": "Phishing"},
    {"ioc": "suspicious-ip", "category": "Reconnaissance"}
]

print("=" * 50)
print("THREAT INTELLIGENCE ENHANCEMENT")
print("=" * 50)

for feed in threat_feeds:

    if feed["category"] == "Malware":
        score = 90

    elif feed["category"] == "Phishing":
        score = 75

    else:
        score = 50

    print(
        f"IOC: {feed['ioc']} | "
        f"Category: {feed['category']} | "
        f"Threat Score: {score}"
    )
