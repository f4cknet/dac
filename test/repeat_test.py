import requests
url = "http://dian683559.shangjia.youzan.com/v4/trade/order/detail/activeRefundBySeller.json"
data = {
    "orderNo":"E20231108153021019502020",
    "itemId":"2973543325993795600",
    'refundFee':100,
    "remark":"h1",
    "disabledTicketCount":0,
    "csrf_token":  "79890787064942522031906239149584115134428696357821353601421249415632810716349"

}

headers = {
    "cookie":"sid=YZ1171868746932174848YZNcXaOryd","X-Service-Chain": '{"name": "prj0070528"}'
}

resp = requests.post(url=url,data=data,headers=headers,proxies={"http":"127.0.0.1:8001"})

print(type(resp.status_code))
print(resp.status_code)
pront