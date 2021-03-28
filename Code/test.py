import pandas as pd
import requests
import json
import urllib.request
from urllib.request import urlopen

def concat_url (api_name,url):
    open_bank_br ={'products-services':'/personal-accounts' , 'discovery':'/status', 'admin':'/metrics','channels':'/branches','other':'' }
    for key,value in open_bank_br.items():
        if key == api_name:
            return url + value

def directory_api_call(base_url):
    r = requests.get(base_url)
    response_json = r.json()
    return response_json

def bank_endpoint_call(endpoint):
    try:
        r = requests.get(endpoint)
        return r.status_code
    except:
        return 404



