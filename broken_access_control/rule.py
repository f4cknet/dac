def check_newrespcode(text):
    pattern = re.compile(r'"code"\s*:\s*502')
    match = pattern.search(text)

    if match:
        return True
    else:
        return False
def check_respcode(text1,text2):
    pattern = re.compile(r'"code"\s*:\s*(\d+)')
    match1 = pattern.search(text1)
    match2 = pattern.search(text2)

    if match1:
        code1 = match1.group(1)
        code2 = match2.group(1)
        if code1 == code2:
            return True
        else:
            return False

def trace_dbcommand_hasupdate(text):

    match = re.search(r'"db\.command": \[[^\]]*"update"[^\]]*\]', text)

    if match:
        result = True
    else:
        result = False

    return result

def trace_tip_noaccess(text):
    if "没有操作权限" in text:
        return False
    else:
        return True

def get_respcode(resp):
    resp_json = json.loads(resp)
    code = resp_json.get('code')
    return code

def check_respcontent(text):
    resp_json = json.loads(text)
    msg = resp_json.get('msg') or ""
    data = resp_json.get('data') or ""
    if msg == "success" or data == True:
        return True
    else:
        return False

def check_old_respcontent(text):
    if "响应已过期" in text:
        return False
    else:
        return True

