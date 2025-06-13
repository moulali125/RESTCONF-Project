import requests
import json
from requests.auth import HTTPBasicAuth

# Replace these variables with your actual device credentials
host = "https://172.20.0.39" 
username = "moulali"
password = "mouli"

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+xml"
}

def restconf_post(url, payload):
    full_url = f"{host}{url}"
    response = requests.post(full_url, headers=headers, data=json.dumps(payload), auth=HTTPBasicAuth(username, password), verify=False)
    if response.status_code in [200, 201, 204]:
        print("POST successful")
    else:
        print(f"POST failed: {response.status_code}")
        print(response.text)

# Payload to create Loopback456 with IP address
payload = {
  "Cisco-IOS-XE-native:Loopback": {
    "name": 456,
    "description": "Created via RESTCONF",
    "ip": {
      "address": {
        "primary": {
          "address": "10.10.10.1",
          "mask": "255.255.255.0"
        }
      }
    }
  }
}

restconf_post("/restconf/data/Cisco-IOS-XE-native:native/interface", payload)

