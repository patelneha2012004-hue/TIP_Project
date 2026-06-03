from datetime import datetime

incidents = [
    {"id": 1, "type": "Malware", "severity": "HIGH"},
    {"id": 2, "type": "Phishing", "severity": "MEDIUM"},
    {"id": 3, "type": "Suspicious Login", "severity": "LOW"}
]

print("=" * 50)
print("INCIDENT RESPONSE SYSTEM")
print("=" * 50)

for incident in incidents:

    print(
        f"\nIncident ID: {incident['id']}"
    )
    print(
        f"Type: {incident['type']}"
    )
    print(
        f"Severity: {incident['severity']}"
    )

    if incident["severity"] == "HIGH":
        action = "Escalate to SOC Team"
    elif incident["severity"] == "MEDIUM":
        action = "Investigate Further"
    else:
        action = "Monitor Activity"

    print(f"Recommended Action: {action}")

print("\nResponse Generated:", datetime.now())
