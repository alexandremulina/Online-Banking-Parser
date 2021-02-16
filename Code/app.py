from flask import Flask, url_for, render_template
import requests
import test

app = Flask(__name__)

@app.route("/")

def home():
    url = 'https://data.directory.openbankingbrasil.org.br/participants'
    response_json = test.directory_api_call(url)
    banks = test.parse_directory_response(response_json)

    for bank in banks:
        print(bank)
        
    return render_template("index.html", content = banks)




if __name__=='__main__':
    app.run()









