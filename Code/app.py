from flask import Flask, url_for, render_template
from flask_caching import Cache
import test
import datetime

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)



@app.route("/")
@cache.cached(timeout=3600) # 1 hour
def home():
    url = 'https://data.directory.openbankingbrasil.org.br/participants'
    # TODO if db data > 2 hours | db is empty:
    # TODO make API calls
    # TODO save on db
    # TODO else:
    # TODO fetch from db (get)
    response_json = test.directory_api_call(url)
    banks = test.parse_directory_response(response_json)
    today = datetime.date.today()
    return render_template("index.html", content = banks, date_time = today)




if __name__=='__main__':
    app.run()









