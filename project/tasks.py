from charles.celery import app
import time


@app.task
def add(x, y):
    print('asds')
    time.sleep(3)
    return x + y
