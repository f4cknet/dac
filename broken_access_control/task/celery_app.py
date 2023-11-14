# 定时任务

import datetime

from celery import Celery
from celery.schedules import crontab

celeryapp = Celery("celey_task",
                    broker="redis://127.0.0.1:6379/2",
                    backend="redis://127.0.0.1:6379/3",
                    include=["broken_access_control.task.start_check"]
                    )
celeryapp.conf.timezone = "Asia/Shanghai"
celeryapp.conf.enable_utc = False
celeryapp.conf.beat_schedule = {
    "start_repeat":{
        "task":"broken_access_control.task.start_check.start_repeat_post",
        "schedule":crontab(minute=30,hour=17),
    }
}
