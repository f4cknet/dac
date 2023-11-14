from broken_access_control.detect_sensitive import *
from broken_access_control.similar import string_similar

def read_check(meta_request,meta_response):
    meta_request_method = get_meta_request_method(meta_request)
    if meta_request_method is "GET":
        if len(detect_backcard.detect_bankno(meta_response))>0 or len(detect_idcard.detect_idcard(meta_response))>0 or len(detect_phone.detect_phone(meta_response))>0:
            host = get_host(meta_request)
            url = get_url(meta_request)
            newcookie = new_cookie(meta_request)
            new_respon_content = requests.get(url=host+url,cookies=newcookie).text
            meta_response_content = get_meta_response_content(meta_response)
            if string_similar(new_respon_content,meta_response_content)>0.9:
                return {"msg":"存在查询越权"}



