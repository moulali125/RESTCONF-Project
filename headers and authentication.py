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
