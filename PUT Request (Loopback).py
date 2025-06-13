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


def restconf_put(url, payload):
    full_url = f"{host}{url}"
    response = requests.put(full_url, headers=headers, data=json.dumps(payload), auth=HTTPBasicAuth(username, password), verify=False)
    if response.status_code in [200, 204]:
        print("PUT successful")
    else:
        print(f"PUT failed: {response.status_code}")
        print(response.text)

# Payload to update IP address of Loopback123
payload = {
  "Cisco-IOS-XE-native:Loopback": {
    "name": 456,
    "ip": {
      "address": {
        "primary": {
          "address": "10.10.10.2",
          "mask": "255.255.255.0"
        }
      }
    }
  }
}

restconf_put("/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=456", payload)
