import requests
from broken_access_control.extract_metaflow import parseFlow
from broken_access_control.reset_authentication import ResetAuthen
from broken_access_control import config

class DacRequest(object):
    def __init__(self,meta_flow):

        self.flow = parseFlow()
        self.meta_flow = meta_flow
        self.old_cookie = self.flow.get_meta_cookie(self.meta_flow)
        self.resetauth = ResetAuthen(self.meta_flow)


    def add_kdtId_body(self):
        # 尝试获取cookie中的kdt_id,并添加到请求body中
        try:
            kdt_id = self.resetauth.get_kdtId_byCookie(self.old_cookie)
            self.flow.get_meta_body(self.meta_flow)['kdtid']=kdt_id
            self.flow.get_meta_body(self.meta_flow)['kdtId']=kdt_id
            self.flow.get_meta_body(self.meta_flow)['kdt_id']=kdt_id
        except:
            pass
        return self.flow.get_meta_body(self.meta_flow)


    def new_header(self):
        header = self.flow.get_meta_header(self.meta_flow)
        header['COOKIE'] = self.resetauth.reset_authen()
        # 元流量经过gzip加密，重放后响应内容都是乱码，所以去掉header中ACCEPT-ENCODING: gzip
        if header.get('ACCEPT-ENCODING'):
            header['ACCEPT-ENCODING'] = ''
        if header.get('X-Service-Chain'):
            header['X-Service-Chain'] = config.sc
        elif header.get('x-service-chain'):
            header['X-Service-Chain'] = config.sc
        else:
            header['X-Service-Chain'] = config.sc

        return header

    def repost(self,endpoint):
        if self.flow.get_meta_method(self.meta_flow) == "POST":
                if "application/x-www-form-urlencoded" in self.flow.get_content_type(self.meta_flow):
                    respon = requests.post(url=endpoint, data=self.add_kdtId_body(),headers=self.new_header(),proxies={"http":"127.0.0.1:8001"})
                    respon.encoding = "utf-8"


                    return respon
                elif "application/json" in self.flow.get_content_type(self.meta_flow):
                    respon = requests.post(url=endpoint, json=self.add_kdtId_body(),headers=self.new_header(),proxies={"http":"127.0.0.1:8001"})
                    respon.encoding = "utf-8"

                    return respon
                else:
                    return self.meta_flow
        else:
            return self.flow.get_meta_method(self.meta_flow)

    def reput(self,endpoint):
        if self.flow.get_meta_method(self.meta_flow) == "PUT":
            if "application/x-www-form-urlencoded" in self.flow.get_content_type(self.meta_flow):
                respon = requests.post(url=endpoint, data=self.add_kdtId_body(),headers=self.new_header())
                respon.encoding = "utf-8"
                return respon.text
            elif "application/json" in self.flow.get_content_type(self.meta_flow):
                respon = requests.post(url=endpoint, json=self.add_kdtId_body(),headers=self.new_header())
                respon.encoding = "utf-8"
                return respon.text
        else:
            return self.flow.get_meta_method(self.meta_flow)

