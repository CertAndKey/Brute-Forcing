#!/usr/bin/env python3
#Bruteforcing API with basic authentication
#this file takes 1 arg which is a list of API endpoints
#this file prints the status code of the get requests
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api_file = "api.txt"

url = "http://<ip_address>"



file = open(api_file,"r")


for api in file:
    api = api.strip()
    url_full = url + api
    
    #GETS
    print("GET "+ url_full)
    r = requests.get(url_full, auth=HTTPBasicAuth('<username>','<password>'))
    print(r.status_code)
    
    #POSTS
    print("POST "+ url_full)
    r = requests.post(url_full, auth=HTTPBasicAuth('<username>','<password>'))
    print(r.status_code)
    
    #PUTS
    print("PUT "+ url_full)
    r = requests.put(url_full, auth=HTTPBasicAuth('<username>','<password>'))
    print(r.status_code)
    
    #PATCHES
    print("PATCH "+ url_full)
    r = requests.patch(url_full, auth=HTTPBasicAuth('<username>','<password>'))
    print(r.status_code)

