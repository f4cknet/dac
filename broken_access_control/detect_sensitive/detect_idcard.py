import re

def detect_idcard(text):
    #匹配中国大陆身份证号码
    id_card_pattern = r'\b(\d{17}[\dXx])\b'
    
    # 使用正则表达式查找身份证号码
    matches = re.findall(id_card_pattern, text)
    
    # 输出检测到的身份证号码
    if matches:
        idcard_list = []
        for id_card in matches:
            idcard_list.append(id_card)
    else:
        print("未检测到身份证号码")

    # 验证身份证有效性，并且超过
    if len(idcard_list)>0:
        vaild_id_cards = []
        start = 0
        for idcard in idcard_list:
            if is_valid_id_card(idcard):
                start+=1
                print("发现明文身份证:"+idcard)
                vaild_id_cards.append(idcard)
                if start>10:
                    print("批量身份证泄漏")   #
                    break
        return vaild_id_cards


def is_valid_id_card(id_card):
    # 地区码验证
    area_code = id_card[:6]
    # TODO: 在国家标准范围内验证area_code

    # 出生日期验证
    birth_date = id_card[6:14]
    year = int(birth_date[:4])
    month = int(birth_date[4:6])
    day = int(birth_date[6:8])
    import datetime
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        return False

    # 校验码验证
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checksum_map = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    checksum = 0
    for i in range(17):
        checksum += int(id_card[i]) * weights[i]
    checksum %= 11
    if id_card[-1] != checksum_map[checksum]:
        return False

    return True


# 测试
if __name__ == "__main__":
    with open('response_text.txt', 'r')as f:
        text = f.read()
        detect_idcard(text)
