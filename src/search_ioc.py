from db_connect import collection

ip = input("Enter IP to search: ")

result = collection.find_one({"ip": ip})

if result:
    print("\n[!] Threat Found")
    print(f"IP: {result['ip']}")
    print(f"Source: {result['source']}")
    print(f"Risk Level: {result['risk']}")
else:
    print("\n[+] No Threat Detected")

