# 这是一个生成验证码文件

# 引入随机数模块
import random

def verificationCode():
    # 定义字符串
    dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # 生成四位验证码
    sum = ""
    for num1 in range(1, 5):
        num = random.randint(1, len(dictionary) - 1)
        sum += dictionary[num]
    print("您的验证码是:%s" % sum)
    return sum
