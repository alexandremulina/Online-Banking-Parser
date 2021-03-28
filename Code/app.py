from flask import Flask, render_template
import test
import datetime
import mongodb
import time
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)




def update():
    mongodb.insert_list()

sched = BackgroundScheduler(daemon=True)
sched.add_job(update,'interval', minutes=5)
sched.start()


app = Flask(__name__)



@app.route("/")
# @cache.cached(timeout=3600) # 1 hour
def home():
    banks = mongodb.export_list()
    today = datetime.date.today()
    return render_template("index.html", content=banks, date_time=today)



# def close_running_threads():
#     for thread in the_threads:
#         thread.join()
#     print "Threads complete, ready to finish"
# #Register the function to be called on exit
# atexit.register(close_running_threads)


if __name__ == '__main__':
    app.run(debug=True)








