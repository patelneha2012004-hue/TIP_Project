from datetime import datetime

HIGH_RISK_KEYWORDS = [
    "malware",
    "ransomware",
    "botnet",
    "phishing",
    "trojan"
]

def optimize_detection(threat_data):
    alerts = []

    for threat in threat_data:
        indicator = threat.lower()

        if any(keyword in indicator for keyword in HIGH_RISK_KEYWORDS):
            alerts.append({
                "threat": threat,
                "severity": "HIGH",
                "timestamp": str(datetime.now())
            })

    return alerts


sample_data = [
    "malware detected from IP",
    "normal traffic",
    "phishing domain found",
    "user login"
]

results = optimize_detection(sample_data)

for alert in results:
    print(alert)
