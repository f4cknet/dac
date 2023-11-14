from dac_write_check import repeat,check
from get_flow import get_existFlow
from extract_metaflow import parseFlow
import datetime
from sql.sql_dml import  insert_repeat_post,select_repeat_ByDate
import datetime,time
import config



parse = parseFlow()

def start_repeat_post(appname,apikey):
    # 串行执行，避免安全策略拦截，或者高并发请求导致的其他访问异常
    traceids = []
    flow_meta = get_existFlow(appname,apikey)
    for meta_flow in flow_meta:
        method = parse.get_meta_method(meta_flow)
        path = parse.get_meta_path(meta_flow)
        params = parse.get_meta_params(meta_flow)
        hash = parse.get_meta_row_key_hash(meta_flow)
        old_resp = parse.get_meta_resp(meta_flow)
        try:
            print()
            resp = repeat(meta_flow)
            print(resp.text)
            header = resp.headers
            new_resp = resp.text
            traceid = header.get('x-yz-trace')
            traceids.append(traceid)
            insert_repeat_post(appname, path, method, str(params), hash, datetime.date.today(), datetime.datetime.now(),
                               datetime.datetime.now(), traceid, str(old_resp), str(new_resp))
        except:
            pass
    return "finish repeat"


def start_check_dac(today):
    check(today)

if __name__ == "__main__":
    appname = config.appname
    apikey = config.apikey
    today = datetime.date.today()
    print(start_repeat_post(appname,apikey))