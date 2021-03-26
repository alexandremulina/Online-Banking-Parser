from flask import Flask, render_template
from celery import group, shared_task
import test
import datetime
import mongodb
from celery import Celery
from celery import task
from flask_caching import Cache
import schedule
import time



app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config['SECRET_KEY']


client = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# client.conf.update(app.config)

@client.task
def update():
    schedule.every(30).minutes.do(mongodb.insert_list())





@app.route("/")
# @cache.cached(timeout=3600) # 1 hour
def home():
    banks = mongodb.export_list()
    today = datetime.date.today()
    # update.apply_async()
    return render_template("index.html", content=banks, date_time=today)





if __name__ == '__main__':
    app.run(debug=True)








