dashboard = {
    "Total Threats": 150,
    "High Risk": 18,
    "Medium Risk": 47,
    "Low Risk": 85
}

print("=" * 50)
print("SOC DASHBOARD SUMMARY")
print("=" * 50)

for key, value in dashboard.items():
    print(f"{key}: {value}")

print("\nSystem Status : ACTIVE")
print("Threat Monitoring : ENABLED")
print("Reporting : SUCCESS")
