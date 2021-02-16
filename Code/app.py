from flask import Flask, url_for, render_template
import requests

app = Flask(__name__)

@app.route("/")

def home():
    for bank in response_json:
        bank_dict = dict()
        bank_dict["name"] = bank['LegalEntityName']
        bank_dict["status"] = bank['Status']
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
                    bank_dict[f"api-{api_family_type}"] = api
                banks.append(bank_dict)
    for index in range(len(banks)):
        print(banks[index]['name'])
        print(banks[index]['status'])
        try:
            url = banks[index]['api-discovery']
            try:
                print('status code :', requests.get(url))
            except requests.exceptions.ConnectionError:
                print("Connection Refused")
        except KeyError:
            url = 'Vazio'
        print(url)
    codes = [r.status_code, r2.status_code]
    results = []
    for code in codes:
        if code == 200:
            results.append('EM FUNCIONAMENTO')
        else:
            results.append('SERVIÇO INSDISPONIVEL')
    return render_template("index.html", content = results)




if __name__=='__main__':
    app.run()









