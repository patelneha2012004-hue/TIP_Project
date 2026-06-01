import time
from datetime import datetime

ioc_list = [
    "malicious-domain.com",
    "phishing-site.net",
    "suspicious-ip-192.168.1.100",
    "ransomware-c2-server.net"
]

print("=" * 50)
print("SOC MONITORING SYSTEM STARTED")
print("=" * 50)

for ioc in ioc_list:
    print(f"[{datetime.now()}] Monitoring IOC: {ioc}")
    time.sleep(1)

print("\nMonitoring Cycle Completed Successfully")
