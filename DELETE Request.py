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

def restconf_delete(url):
    full_url = f"{host}{url}"
    response = requests.delete(full_url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    if response.status_code in [200, 204]:
        print("DELETE successful")
    else:
        print(f"DELETE failed: {response.status_code}")
        print(response.text)

# Example usage: Delete Loopback123
restconf_delete("/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=456")
