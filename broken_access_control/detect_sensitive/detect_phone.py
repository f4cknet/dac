import re

def detect_phone(text):
    phone_number_pattern = r'\b(1[356789]\d{9})\b'
    sensitive_info = []
    phone_numbers = re.findall(phone_number_pattern, text)

    if phone_numbers:
        return phone_numbers

if __name__ == "__main__":
    fp = open('response_text.txt', 'r')
    content = fp.read()
    fp.close()
    phone = detect_phone(content)
    if phone:
        print("发现明文手机号:")
        print(phone)
        # for info_field in sensitive_info:
        #     print(info)
    else:
        print("未发现敏感信息")