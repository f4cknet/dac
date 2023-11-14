import callapi
import config
import json

class TechapiSetting(object):
    SOURCE_APP_NAME = ''
    TECHAPI_MD5_KEY = ''

def get_interface_list(appname,apikey):
    api_url =  '{}/api/v1/interfaces'.format(config.interface_endpoint)
    resp = _call_api(
        TechapiSetting,
        api_url,
        'GET',
        {"app":appname,"apikey":apikey,"type":"http","page":1,"per_page":1000},
    )
    interface_list = json.loads(resp)
    value = interface_list.get('data').get('value')
    return value

def get_flow_byInterfaceId(id,page):
    domain = config.interface_endpoint
    api_url = config.interface_sample_url
    resp = callapi(
        TechapiSetting,
        api_url,
        'GET',
        {'page':page},
    )
    return resp

def get_existFlow(appname,apikey):
    flows = []
    interface_list = get_interface_list(appname, apikey)
    for interface in interface_list:
        interface_id = interface.get("id")
        flow = get_flow_byInterfaceId(interface_id,1)
        flow_json = json.loads(flow)


        data = flow_json.get("data")
        if data.get("total")>0:
           page = 1
           total = data.get("total")
           while page<=total:
               flow = get_flow_byInterfaceId(interface_id,page)
               flow_json = json.loads(flow)
               data = flow_json.get("data")
               items = data.get("items")
               flows.append(items[0])
               page+=1
    return flows



if __name__ == "__main__":
    pass


