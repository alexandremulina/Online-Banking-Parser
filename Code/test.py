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

def parse_directory_response(response_json):
    banks = []
    for bank in response_json:
        bank_dict = dict()
        bank_dict["name"] = bank['LegalEntityName']
        bank_dict["status"] = bank['Status']
        bank_dict["api_resources"] = []
        auth_servers = bank['AuthorisationServers']
        for server in auth_servers:
            api_resources = server['ApiResources']
            if api_resources is not None:
                for api_resource in api_resources:
                    api_family_type = api_resource['ApiFamilyType']
                    try:
                        api = api_resource['ApiDiscoveryEndpoints'][0]['ApiEndpoint']
                    except IndexError:
                        api = None
                    if api:
                        endpoint = concat_url(api_family_type, api)
                        endpoint_status = bank_endpoint_call(endpoint)
                        api_dict = {f"api-{api_family_type}": {'url': endpoint, 'status': endpoint_status}}
                    else:
                        api_dict = {f"api-{api_family_type}": {'url': 'none', 'status': 'none'}}
                    bank_dict["api_resources"].append(api_dict)
                banks.append(bank_dict)
    return banks


