#!/usr/bin/env python3

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api_file = "api.txt"

url = "http://192.168.1.30"



file = open(api_file,"r")


for api in file:
    api = api.strip()
    url_full = url + api
    print(url_full)
    r = requests.get(url_full, auth=HTTPBasicAuth('admin','password1'))
    print(r.status_code)

