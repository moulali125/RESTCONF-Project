import requests
import json
from requests.auth import HTTPBasicAuth

# Replace these variables with your actual device credentials
host = "https://172.20.0.39" 
username = "moulali"
password = "mouli"

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

# Disable SSL warnings (use only in dev/test environments)
requests.packages.urllib3.disable_warnings()

def restconf_get(url):
    full_url = f"{host}{url}"
    response = requests.get(full_url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    if response.status_code == 200:
        print(f"\nGET Successful: {url}")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"\nGET failed: {response.status_code}")
        print(response.text)

# --- Menu of useful RESTCONF resources ---
resource_paths = {
    "1": ("/restconf/data/Cisco-IOS-XE-native:native/interface", "Interfaces"),
    "2": ("/restconf/data/Cisco-IOS-XE-native:native/ip/route", "Static Config"),
    "3": ("/restconf/data/Cisco-IOS-XE-native:native", "Full Native Config"),
    "4": ("/restconf/data/Cisco-IOS-XE-native:native/hostname", "Hostname"),
    "5": ("/restconf/data/netconf-state/capabilities", "Capabilities (IETF YANG)"),
}

# --- Simple CLI menu ---
print("\nSelect resource to GET:")
for key, (_, description) in resource_paths.items():
    print(f"{key}. {description}")

choice = input("Enter choice: ").strip()

if choice in resource_paths:
    url, description = resource_paths[choice]
    print(f"\nGetting {description} ...")
    restconf_get(url)
else:
    print("Invalid choice.")
