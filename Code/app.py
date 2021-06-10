from flask import Flask, render_template
import atexit
import test
import datetime
import mongodb
from apscheduler.schedulers.background import BackgroundScheduler
from flask_caching import Cache
import time

#caching
config = {
    "DEBUG":True,
    "CACHE_TYPE":"simple",
    "CACHE_DEFAULT_TIMEOUT":300
}


def update():
    mongodb.insert_list()


def last_time():
    return time.ctime()

sched = BackgroundScheduler(daemon=True)
sched.add_job(update,'interval', minutes=10)
sched.start()


app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)



@app.route("/")
@cache.cached(timeout=180)
def home():
    banks = mongodb.export_list()
    today = mongodb.last_update()
    return render_template("index.html", content=banks, date_time=today )



if __name__ == '__main__':
    app.run(debug=True)








