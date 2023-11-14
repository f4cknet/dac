import requests
endpoint = "/v4/trade/shopAddress/detail.json"

url = "http://dian101132104.shangjia.youzan.com"+endpoint
headers = {"sid":"YZ1173641578527735808YZpqozDlrS"}

data={
         "contactName":"%E4%B9%90%E5%8D%A1%E4%BB%93%E5%BA%93",
    "countryIndex":0,
    "mobilePhone":"18781250369",
    "regionType":"china",
    "address":"%E6%96%B0%E7%A2%B6%E8%A1%97%E9%81%93%E6%B5%99%E6%B1%9F%E7%9C%81%E5%AE%81%E6%B3%A2%E5%B8%82%E5%8C%97%E4%BB%91%E5%8C%BA%E6%96%B0%E5%A5%91%E8%A1%97%E9%81%93%E4%B9%9D%E5%8D%8E%E5%B1%B1%E8%B7%AF402%E5%8F%B73%E6%A5%BC",
    "countyId":"330206",
    "province":"%E6%B5%99%E6%B1%9F%E7%9C%81",
    "city":"%E5%AE%81%E6%B3%A2%E5%B8%82",
    "county":"%E5%8C%97%E4%BB%91%E5%8C%BA",
    "addressTypes%5B0%5D%5BaddressType%5D":1,
     "addressTypes%5B0%5D%5BisDefault%5D":False,
    "csrf_token":"92803966428910502865480342418805892415193634107807310419737460578651054287261"
}

reson = requests.get(url=url,headers=headers,proxies={'http':'127.0.0.1'})

print(reson.text)
print(type(reson.status_code))