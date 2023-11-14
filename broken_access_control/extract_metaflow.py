from broken_access_control.get_flow import get_existFlow
from urllib.parse import parse_qs
from hashlib import md5
import json


class parseFlow(object):

    def get_meta_resp(self,meta_flow):
        return meta_flow.get("resp")

    def get_content_type(self,meta_flow):
        return meta_flow.get('headers').get('CONTENT-TYPE')

    def get_meta_method(self,meta_flow):
        return meta_flow.get("method")
    def get_meta_header(self,meta_flow):
        return meta_flow.get("headers")

    def get_meta_host(self,meta_flow):
        return meta_flow.get("headers").get('HOST')
    def get_meta_traceid(self,meta_flow):
        return meta_flow.get('headers').get('X-YZ-TRACE')

    def get_meta_row_key_hash(self,meta_flow):
        return meta_flow.get('row_key_hash')

    def get_meta_path(self,meta_flow):
        return meta_flow.get("path")
    def get_meta_params(self,meta_flow):
        body = self.get_meta_body(meta_flow)
        keynames = body.keys()
        key_list = list(keynames)
        key_list.sort()
        return key_list
    def get_meta_cookie(self,meta_flow):
        return meta_flow.get('headers').get('COOKIE')
    def get_meta_body(self,meta_flow):
        json_body = {}
        body = meta_flow.get("body")
        if self.get_content_type(meta_flow):
            if "application/x-www-form-urlencoded" in self.get_content_type(meta_flow):
                data = parse_qs(body).items()
                for key,value in data:
                    json_body.update({key:value[0]})

            elif  "application/json" in self.get_content_type(meta_flow):
                body = meta_flow.get("body")
                json_body = json.loads(body)
        return json_body



if __name__ == "__main__":
    meta_flows=get_existFlow("wsc-pc-trade","POST")
    metaflows = parseFlow()
    for metaflow in meta_flows:
        metaflow_header = metaflows.get_meta_header(metaflow)
        metaflow_host = metaflows.get_meta_host(metaflow)
        metaflow_path = metaflows.get_meta_path(metaflow)
        metaflow_body = metaflows.get_meta_body(metaflow)
        metaflow_method = metaflows.get_meta_method(metaflow)
        metaflow_resp = metaflows.get_meta_resp(metaflow)
        metaflow_content_type = metaflows.get_content_type(metaflow)
        metaflow_cookie = metaflows.get_meta_cookie(metaflow)
        print(metaflow_host,metaflow_path,metaflow_resp)
    #print(metaflow_method+" https://" +metaflow_host+metaflow_path+'\n'+metaflow_body)



