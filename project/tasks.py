from celery import Task

from charles.celery import app
import time


class CallbackTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('callback11',retval, task_id, args, kwargs,end=',')

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(exc, task_id, args, kwargs, einfo)


@app.task(base=CallbackTask)
def add(x, y):
    print('asds')
    return x + y
