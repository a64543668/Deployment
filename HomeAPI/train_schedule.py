from query import load_data
from helpers import split_df
from model import clf_model
from threading import Timer

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz as tz
import time

CT = tz.timezone('US/Eastern')
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='wed', hour=14, minute=50, timezone=CT)
def train_model_scheduler():
    print('Re-train the model')
    df=load_data()
    X_train, X_test, y_train, y_test=split_df(df)
    model=clf_model(X_train, y_train)

sched.start()


