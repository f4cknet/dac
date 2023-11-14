import re

def detect_bankno(text):
    bank_card_pattern = r'(\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{0,4})'
    matches = re.findall(bank_card_pattern, text)
    if matches:
        print("检测到的银行卡号:")
        bankNo_list = []
        for bank_card in matches:
            # 去除空格和连字符
            bank_card = bank_card.replace(" ", "").replace("-", "")


            # 验证银行卡号有效性（使用Luhn算法）
            def is_valid_luhn(card_number):
                digits = [int(x) for x in card_number]
                checksum = digits[-1]
                digits = digits[:-1][::-1]
                for i in range(len(digits)):
                    if i % 2 == 0:
                        digits[i] *= 2
                        if digits[i] > 9:
                            digits[i] -= 9
                total = sum(digits)
                return (total + checksum) % 10 == 0


            if is_valid_luhn(bank_card):
                print(f"银行卡号: {bank_card} (有效)")
                bankNo_list.append(bank_card)
            else:
                print(f"银行卡号: {bank_card} (无效)")
    else:
        print("未检测到银行卡号")
    return bankNo_list

if __name__ == "__main__":
    with open('response_text.txt', 'r')as f:
        text=f.read()
        result = detect_bankno(text)
    print(result)