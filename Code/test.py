import pandas as pd
import requests
import json
import urllib.request
from urllib.request import urlopen

url = 'https://data.directory.openbankingbrasil.org.br/participants'
# header = {
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
#         "X-Requested-With": "XMLHttpRequest"
#         }
counter = 0
r = requests.get(url)
response_json = r.json()
banks = []

# response = urlopen(url)

for bank in response_json:
    bank_dict = dict()
    bank_dict["name"] = bank['LegalEntityName']
    bank_dict["status"] = bank['Status']
    print(bank['LegalEntityName'])
    auth_servers = bank['AuthorisationServers']
    for server in auth_servers:
        api_resources = server['ApiResources']
        if api_resources is not None:
            for api_resource in api_resources:
                api_family_type = api_resource['ApiFamilyType']
                try:
                    api = api_resource['ApiDiscoveryEndpoints'][0]['ApiEndpoint']
                except IndexError:
                    api = 'http://Null'
                # print(api_family_type)
                # print(api)
                bank_dict[f"api-{api_family_type}"] = api
            banks.append(bank_dict)

print('-------------------------------------------------------')
print(len(response_json))
print(banks)

for index in range(len(banks)):
    print(banks[index]['name'])
    print(banks[index]['status'])
    try:
        url = banks[index]['api-discovery']
        url1 = banks[index]['api-products-services']
        url2 = banks[index]['api-admin']
        url3 = banks[index]['api-channels']
        # url4 = banks[index]['api-other']
        try:
            print('status code :',requests.get(url))
            print('status code :', requests.get(url1))
            print('status code :', requests.get(url2))
            print('status code :', requests.get(url3))
            # print('status code :', requests.get(url4))

        except (requests.exceptions.ConnectionError):
            print("Connection Refused")
    except KeyError:
        url = 'Vazio'
        url1 = 'Vazio'
        url2 = 'Vazio'
        url3 = 'Vazio'
        # url4 = 'Vazio'

    print(url)
    print(url1)
    print(url2)
    print(url3)
    # print(url4)



# a= banks[1].values()
# b = banks[1].keys()
# print (a)
# print(b)
# dict_keys(['name', 'status', 'api-discovery', 'api-products-services', 'api-admin', 'api-channels'])