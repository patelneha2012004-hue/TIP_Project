from datetime import datetime

threats = [
    {"ioc": "malicious-domain.com", "severity": "HIGH"},
    {"ioc": "192.168.1.10", "severity": "LOW"},
    {"ioc": "phishing-site.net", "severity": "HIGH"},
    {"ioc": "suspicious-ip.net", "severity": "MEDIUM"}
]

print("=" * 40)
print("THREAT INTELLIGENCE DAILY REPORT")
print("=" * 40)
print("Generated:", datetime.now())

high = 0
medium = 0
low = 0

for threat in threats:

    if threat["severity"] == "HIGH":
        high += 1
    elif threat["severity"] == "MEDIUM":
        medium += 1
    else:
        low += 1

    print(
        f"IOC: {threat['ioc']} | Severity: {threat['severity']}"
    )

print("\nSUMMARY")
print("Total Threats:", len(threats))
print("High Risk:", high)
print("Medium Risk:", medium)
print("Low Risk:", low)
