import xadmin
from djcelery.models import (
    TaskState, WorkerState,
    PeriodicTask, IntervalSchedule, CrontabSchedule,
)

from .models import Project


# Register your models here.

class PeopleAdmin(object):
    list_display = ["id", "offer_title", "relative_url", 'date_created', 'popular_ordering']


xadmin.site.register(Project, PeopleAdmin)

xadmin.site.register(IntervalSchedule)  # 存储循环任务设置的时间
xadmin.site.register(CrontabSchedule)  # 存储定时任务设置的时间
xadmin.site.register(PeriodicTask)  # 存储任务
xadmin.site.register(TaskState)  # 存储任务执行状态
xadmin.site.register(WorkerState)  # 存储执行任务的worker
