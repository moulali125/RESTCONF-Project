import requests
import json
from requests.auth import HTTPBasicAuth

host = "https://172.20.0.39"
username = "moulali"
password = "mouli"

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

requests.packages.urllib3.disable_warnings()

def restconf_put(url, payload):
    full_url = f"{host}{url}"
    response = requests.put(full_url, headers=headers, data=json.dumps(payload),
                            auth=HTTPBasicAuth(username, password), verify=False)

    print(f"PUT to {full_url}")
    print(f"Payload:\n{json.dumps(payload, indent=2)}")

    if response.status_code in [200, 201, 204]:
        print("PUT successful")
    else:
        print(f"PUT failed: {response.status_code}")
        print(response.text)

# Static route payload
static_route_payload = {
    "Cisco-IOS-XE-native:route": {
        "ip-route-interface-forwarding-list": [
            {
                "prefix": "192.168.2.0",
                "mask": "255.255.255.0",
                "fwd-list": [
                    {
                        "fwd": "192.168.1.2"
                    }
                ]
            }
        ]
    }
}

if __name__ == "__main__":
    restconf_put("/restconf/data/Cisco-IOS-XE-native:native/ip/route", static_route_payload)
