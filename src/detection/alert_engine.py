from detection_rules import (
    is_high_risk_ip,
    is_malicious_domain,
    is_high_risk_score
)

sample_data = [
    {
        "ip": "185.220.101.1",
        "domain": "safe.com",
        "risk_score": 95
    },
    {
        "ip": "8.8.8.8",
        "domain": "malware-test.com",
        "risk_score": 85
    }
]

for threat in sample_data:

    if is_high_risk_ip(threat["ip"]):
        print(f"[ALERT] High Risk IP Detected: {threat['ip']}")

    if is_malicious_domain(threat["domain"]):
        print(f"[ALERT] Malicious Domain Detected: {threat['domain']}")

    if is_high_risk_score(threat["risk_score"]):
        print(f"[ALERT] High Risk Score: {threat['risk_score']}")

