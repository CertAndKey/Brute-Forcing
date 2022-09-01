#!/usr/bin/env python3
#Bruteforcing API with digest authentication
#this file takes 1 arg which is a list of API endpoints
#this file prints the status code of the get requests
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPDigestAuth

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api_file = "api.txt"

url = "http://<ip_address>"

file = open(api_file,"r")

for api in file:
    api = api.strip()
    url_full = url + api
    print(url_full)
    r = requests.get(url_full, auth=HTTPDigestAuth('<username>','<password>'))
    print(r.status_code)
