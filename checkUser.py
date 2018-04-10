# 这是一个检查用户名和密码是否符合规范的文件
# 用户名长度必须大于6位,必须包含数字以及英文字母
# 密码长度必须大于8位,必须包含数字英文字母以及下划线

# 定义一个检查用户规范的函数
def checkUsername(str):
    # 定义布尔型变量
    a = False
    b = False
    # 判断字符串的长度是否够
    if len(str) > 6:
        # 变量字符串
        for x in str:
            # 判断字符串内是否包含数字
            if x.isdigit():
                a = True
            # 判断字符串内是否包含字母
            if x.isalpha():
                b = True
        if a and b:
            return True
        else:
            return False
    else:
        return False

# 定义一个检查密码规范的函数
def checkPassword(str):
    # 定义布尔型变量
    a = False
    b = False
    c = False
    # 判断密码的长度是否够
    if len(str) > 8:
        # 遍历字符串
        for x in str:
            # 判断字符串内是否包含数字
            if x.isdigit():
                a = True
             # 判断字符串内是否包含字母
            if x.isalpha():
                b = True
        # 判断字符串内是否包含下划线或美元符号
        if str.find("_") != -1 or str.find("$") != -1:
            c = True
        if a and b and c:
            return True
        else:
            return False
    else:
        return False
