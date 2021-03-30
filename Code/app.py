from flask import Flask, render_template
import atexit
import test
import datetime
import mongodb
from apscheduler.schedulers.background import BackgroundScheduler
from flask_caching import Cache

#caching
config = {
    "DEBUG":True,
    "CACHE_TYPE":"simple",
    "CACHE_DEFAULT_TIMEOUT":300
}


def update():
    mongodb.insert_list()

sched = BackgroundScheduler(daemon=True)
sched.add_job(update,'interval', minutes=60)
sched.start()


app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)



@app.route("/")
@cache.cached(timeout=3900)
def home():
    banks = mongodb.export_list()
    today = datetime.date.today()
    return render_template("index.html", content=banks, date_time=today)



if __name__ == '__main__':
    app.run(debug=True)








