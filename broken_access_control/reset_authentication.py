import re
from broken_access_control.extract_metaflow import parseFlow
from broken_access_control import config
class ResetAuthen(object):
    def __init__(self,meta_flow):
        self.cookie = parseFlow().get_meta_cookie(meta_flow)
    def reset_authen(self):
        match_sid = re.search(r'sid=([^;]+)', self.cookie)
        match_kdtsessionid = re.search(r'KDTSESSIONID=([^;]+)', self.cookie)
        match_access_token = re.search(r'access_token=([^;]+)', self.cookie)
        if match_sid:
            old_sid_value = match_sid.group(1)
            self.cookie = re.sub(r'sid=' + re.escape(old_sid_value), 'sid=' + config.new_sid, self.cookie)
        if match_kdtsessionid:
            old_kdtsessionid_value = match_kdtsessionid.group(1)
            self.cookie = re.sub(r'KDTSESSIONID=' + re.escape(old_kdtsessionid_value), 'KDTSESSIONID=' + config.new_sessionid, self.cookie)
        if match_access_token:
            old_access_token_value = match_access_token.group(1)
            self.cookie = re.sub(r'access_token=' + re.escape(old_access_token_value), 'sid=' + config.new_access_token, self.cookie)

        return self.cookie


    def reset_kdtsessionid(self,cookie):
        match = re.search(r'KDTSESSIONID=([^;]+)', cookie)
        if match:
            old_kdtsessionid_value = match.group(1)
            new_kdtsessionid_value = self.get_new_kdtsessionid()
            new_cookie = re.sub(r'KDTSESSIONID=' + re.escape(old_kdtsessionid_value), 'sid=' + new_kdtsessionid_value, cookie)
            return new_cookie
        else:
            return cookie

    def reset_access_token(self,cookie):
        match = re.search(r'access_token=([^;]+)', cookie)
        if match:
            old_access_token_value = match.group(1)
            new_access_token_value = self.get_new_access_token()
            new_cookie = re.sub(r'access_token=' + re.escape(old_access_token_value), 'sid=' + new_access_token_value, cookie)
            return new_cookie
        else:
            return cookie
    def get_kdtId_byCookie(cookie):
        match = re.search(r'kdt_id=([^;]+)',cookie)
        if match:
            kdt_id = match.group(1)
            return kdt_id
