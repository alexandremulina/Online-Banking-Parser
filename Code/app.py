from flask import Flask, url_for, render_template
import requests

app = Flask(__name__)

@app.route("/")

def home():
    r = requests.get("https://api.itau/open-banking/channels/v1/branches")
    r2 = requests.get("https://api.bradesco.com/bradesco/open-banking/channels/v1/branche")
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









