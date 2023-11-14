# coding: utf-8
import os,sys
import time

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.insert(0,root_path)
from broken_access_control.request_overwrite import DacRequest
from broken_access_control.extract_metaflow import parseFlow
from broken_access_control.get_flow import get_existFlow
from broken_access_control.sql.sql_dml import select_repeat_ByDate,update_dac_result,select_oldrespAndnewresp_ByTraceId
import datetime,requests,re,json
from broken_access_control.similar import string_similar
from broken_access_control import config
from broken_access_control.rule import  *

# request = DacRequest()
parse = parseFlow()
def repeat(meta_flow):
    method = parse.get_meta_method(meta_flow)
    host = parse.get_meta_host(meta_flow)
    path = parse.get_meta_path(meta_flow)
    endpoint = f"http://{host}{path}"
    request = DacRequest(meta_flow)
    if method == "POST":
        result = request.repost(endpoint=endpoint)
    elif method == "PUT":
        result = request.reput(endpoint=endpoint)
    else:
        result = "error"
    return result

def check(dat):
    endpoint = config.ops_traceid_endpoint
    header = {
        "RontgenEnv": "qa",
        "buId": "1",
        "Authorization": config.ops_jwt
    }
    query_data = select_repeat_ByDate(dat,config.appname)
    num = 0
    for traceid,hash in query_data:
        num+=1
        url = endpoint+traceid

        resp = requests.get(url=url,headers = header)
        resp_text = resp.text
        # 这里有很多父节点和子节点，子节点下面还有子节点，用循环便利出所有节点太慢了，直接用正则匹配是否存在db.command["update"]或者db.command["select","update"]
        if trace_dbcommand_hasupdate(resp_text) is True:
            print("链路中有update操作，判断为越权")
            update_dac_result(traceid,1,"链路中有update操作",hash,dat) # 1表示有数据update越权操作漏洞
        else:
            if not trace_tip_noaccess(resp_text):
                print("链路中有logging：没有操作权限，判断为非越权")
                update_dac_result(traceid,0,"链路中提示:没有操作权限",hash,dat)
            else:
                resp_results = select_oldrespAndnewresp_ByTraceId(hash)
                for resp_result in resp_results:
                    if check_newrespcode(str(resp_result[1])):
                        print("重放响应状态码是502错误，需要人工进一步判断")
                        update_dac_result(traceid,2,"响应code502，需要人工判断",hash,dat)
                    elif check_respcontent(str(resp_result[1])):
                        print("重放响应中有success,true内容，判断为越权")
                        update_dac_result(traceid,1,"重返响应成功，存在越权",hash,dat)
                    elif get_respcode(str(resp_result[1]))==10302:
                        print("重放响应状态为10302，判断为没有权限 ")
                        update_dac_result(traceid,0,"响应状态码10302，身份验证失败，判断为非越权",hash,dat)


                    else:
                        # print(resp_result[0],resp_result[1])
                        if string_similar(str(resp_result[0]),str(resp_result[1]))>0.8:
                            if check_respcode(str(resp_result[0]),str(resp_result[1])):
                                update_dac_result(traceid, 2,"原始状态码和重放状态码一样，可能存在越权",hash,dat)
                                print("原始状态码和重放状态码一样，可能存在越权")

                            else:
                                print("状态码不一样，不存在越权")
                                update_dac_result(traceid,0,"状态码不一样，不存在越权",hash,date)
                        else:
                            update_dac_result(traceid, 0, "原始响应和重放响应相似度小于0.8",hash,date)
                    # time.sleep(1)

    print(num)

    return "finish check"











if __name__ == '__main__':
    pass


