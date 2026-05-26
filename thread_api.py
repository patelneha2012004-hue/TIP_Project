import requests

# VirusTotal API Key
VT_API_KEY = "70aa88de9736ab747e6b20177bce8ccc26e9762ef00af5d4edb1b7c88617ee26"

def check_virustotal(ip):

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    headers = {
        "x-apikey": VT_API_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    print("\n===== VirusTotal Result =====")

    try:
        stats = data["data"]["attributes"]["last_analysis_stats"]

        print("Malicious :", stats["malicious"])
        print("Suspicious:", stats["suspicious"])
        print("Harmless  :", stats["harmless"])

    except:
        print("Error or Invalid API Key")


if __name__ == "__main__":

    ip = input("Enter IP Address: ")

    check_virustotal(ip)
