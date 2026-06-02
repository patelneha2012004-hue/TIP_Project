sample_logs = [
    "INFO User login successful",
    "WARNING Multiple failed login attempts",
    "ERROR Suspicious IP detected",
    "INFO File accessed",
    "ERROR Malware signature detected"
]

print("=" * 50)
print("LOG ANALYSIS SYSTEM")
print("=" * 50)

for log in sample_logs:
    print(log)

print("\nSuspicious Events Found:")

for log in sample_logs:
    if "ERROR" in log or "WARNING" in log:
        print(log)
