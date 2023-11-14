import re
import spacy

# 示例响应内容
response_content = '''
"buyer": {
    "country_code": "+86",
    "phone": "13655719712",
    "nick_name": "13655719712",
    "mobile": "13655719712",
    "id": 17231580653,
    "account": "+86-13655719712",
    "require_password": false,
    "adr": "浙江省杭州市滨江区中心花园12幢1单元401"
}
'''

# 初始化spaCy模型
nlp = spacy.load("zh_core_web_sm")

# 使用spaCy解析文本并查找地址
def find_address(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":  # GPE表示地理政治实体，通常包括地址信息
            return ent.text
    return None

if __name__ == "__main__":
    address = find_address(response_content)
    if address:
        print("发现明文住址:")
        print(address)
    else:
        print("未发现明文住址")
