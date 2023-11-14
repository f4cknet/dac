from urllib.parse import parse_qs
import json

def www_form_urlencoded():
    a = "labelName=48%E4%BA%94%E9%83%A8%E4%BB%81%E7%9F%A5%E9%BA%A6%E6%9C%B5\u0026id=24560\u0026csrf_token=76166435574079665064742310105996408576907547276619102799105926804963707791772"
    res = parse_qs(a)
    keyname = res.keys()
    for key in keyname:
        print(key)

def application_json():
    body = "{\"contactName\":\"137******64\",\"provinceName\":\"广东省\",\"countyName\":\"龙湖区\",\"cityName\":\"汕头市\",\"idCard\":\"\",\"lng\":\"113.71565700000\",\"lat\":\"22.998877\",\"phone\":\"13002154125\",\"positionSource\":2,\"stationAddress\":\"汕融大厦\",\"stationName\":\"微商城单店测试1\",\"business\":1,\"csrf_token\":\"69628139823850202177141631620280966749557455923008780683988323001529073354621\"}"
    json_obj = json.loads(body)
    keynames = json_obj.keys()
    key_list = list(keynames)
    key_list.sort()
    allkey = ''.join(key_list)
    print(allkey)

application_json()