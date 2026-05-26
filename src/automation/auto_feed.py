import requests

THREAT_FEED_URL = "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"

def fetch_threat_feed():

    print("[+] Fetching Threat Feed...")

    response = requests.get(THREAT_FEED_URL)

    if response.status_code == 200:

        print("[+] Threat Feed Downloaded Successfully")

        lines = response.text.splitlines()

        print(f"[+] Total Threat IOCs Collected: {len(lines)}")

    else:

        print("[-] Failed To Fetch Threat Feed")

fetch_threat_feed()
