import pandas as pd
import requests
import json
import urllib.request
from urllib.request import urlopen

def directory_api_call(base_url):
    r = requests.get(base_url)
    response_json = r.json()
    return response_json

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
                        api = 'Null'
                    api_dict = {f"api-{api_family_type}": api}
                    bank_dict["api_resources"].append(api_dict)
                banks.append(bank_dict)
    return banks