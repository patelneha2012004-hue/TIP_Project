import time

threats = [
    "malware-domain.com",
    "phishing-site.net",
    "suspicious-ip",
    "ransomware-c2",
    "trojan-host"
]

print("=" * 50)
print("SIEM PERFORMANCE OPTIMIZATION")
print("=" * 50)

start_time = time.time()

for threat in threats:
    print(f"Searching IOC: {threat}")

end_time = time.time()

print("\nSearch Completed")
print(
    f"Execution Time: {end_time - start_time:.5f} seconds"
)
