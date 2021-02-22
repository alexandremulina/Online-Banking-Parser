from flask import Flask, url_for, render_template
import requests
import test
import datetime

app = Flask(__name__)

@app.route("/")



def home():
    url = 'https://data.directory.openbankingbrasil.org.br/participants'
    response_json = test.directory_api_call(url)
    banks = test.parse_directory_response(response_json)
    today = datetime.date.today()
    print(banks)
    return render_template("index.html", content = banks, date_time = today)




if __name__=='__main__':
    app.run()









