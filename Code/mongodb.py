import pymongo
from pymongo import MongoClient
import test
import time



cluster = MongoClient("mongodb+srv://alexandre:alexandre@cluster0.zqfw2.mongodb.net/Bank?retryWrites=true&w=majority")

db = cluster["Bank"]
collection = db["Bank"]

def erase_db():
    collection.delete_many({})
    pass

def export_list():
    banks=[]
    cursor = collection.find({})
    for document in cursor:
        banks.append(document)
    return banks

def insert_list():
    url = 'https://data.directory.openbankingbrasil.org.br/participants'
    response_json = test.directory_api_call(url)
    erase_db()
    for bank in response_json:
        bank_dict = dict()
        bank_dict["api_resources"] = []
        for server in bank['AuthorisationServers']:
            api_resources = server['ApiResources']
            if api_resources is not None:
                for api_resource in api_resources:
                    api_family_type = api_resource['ApiFamilyType']
                    try:
                        api = api_resource['ApiDiscoveryEndpoints'][0]['ApiEndpoint']
                    except IndexError:
                        api = None
                    if api:
                        endpoint = test.concat_url(api_family_type, api)
                        endpoint_status = test.bank_endpoint_call(endpoint)
                        api_dict = {f"api-{api_family_type}": {'url': endpoint, 'status': endpoint_status}}
                    else:
                        api_dict = {f"api-{api_family_type}": {'url': 'none', 'status': 'none'}}
                    bank_dict["api_resources"].append(api_dict)
                collection.insert_one({"name":bank['LegalEntityName'],"status":bank['Status'],"api_resources":bank_dict["api_resources"]})
    return print("DB Atualizado")

def last_update():
    lasted=list(collection.find().sort("_id", pymongo.DESCENDING).limit(1))
    return lasted[0]['_id'].generation_time