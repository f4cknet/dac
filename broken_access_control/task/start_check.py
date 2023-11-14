from broken_access_control.dac_write_check import repeat
from broken_access_control.get_flow import get_existFlow
from broken_access_control.task.celery_app import celeryapp
from broken_access_control.sql.sql_dml import insert_repeat_post
from broken_access_control.extract_metaflow import parseFlow
from datetime import datetime


parse = parseFlow()
@celeryapp.task
def start_repeat_post(appname,apikey):
    # 串行执行，避免安全策略拦截，或者高并发请求导致的其他访问异常
    traceids = []
    for meta_flow in get_existFlow(appname,apikey):
        method = parse.get_meta_method(meta_flow)
        path = parse.get_meta_path(meta_flow)
        params = parse.get_meta_params(meta_flow)
        hash = parse.get_meta_hash(meta_flow)
        old_resp = parse.get_meta_resp(meta_flow)
        old_traceid = parse.get_
        resp = repeat(meta_flow)
        header = resp.headers
        new_resp = resp.text
        traceid = header.get('x-yz-trace')
        traceids.append(traceid)
        insert_repeat_post(path,method,str(params),hash,datetime.now(),traceid,old_traceid,str(old_resp),str(new_resp))
    return "finish repeat"


