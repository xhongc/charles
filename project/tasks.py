import os

from celery import Task

from charles.celery import app
from project.utils import upload_qiniu, HomePageCut


class CallbackTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('callback11', retval, task_id, args, kwargs, end=',')

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(exc, task_id, args, kwargs, einfo)


@app.task(base=CallbackTask)
def add(x, y):
    print('asds')
    return x + y


@app.task(base=CallbackTask)
def catch_home(url, uid):
    is_success = HomePageCut().cut(url, out='out.png')
    if is_success:
        upload_qiniu(url, uid)


@app.task(base=CallbackTask)
def catch_home_task():
    from charles.navi.models import Nana

    nanas = Nana.objects.filter(img_path='/', url__isnull=False).values('url', 'id')
    for each in nanas:
        url = each.get('url', '')
        uid = each.get('id', '')
        print('catch', url)
        is_success = HomePageCut().cut(url, out='out.png')
        if is_success:
            upload_qiniu(uid, uid)


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charles.settings')
    upload_qiniu('test2', '1239')
