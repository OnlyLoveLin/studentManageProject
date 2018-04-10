# 这是一个注册函数


# 导入需要的模块:

# 导入需要的自定义模块
import Teacher
import Io
import checkUser
import verificationCode


def regist():
    while True:
        try:
            teacherList = Io.TeacherIo().read_teacher()
        except:
            teacherList = []
        print(" 用户名长度必须大于6位,必须包含数字以及英文字母")
        print("密码长度必须大于8位,必须包含数字英文字母以及下划线")
        # 定义一个布尔型变量
        b1 = True
        # 从键盘读入用户名
        teacher_id = input("请输入您的用户名(按r键退出):")
        if teacher_id == "r":
            break
        else:
            # 检查用户名是否符合规范
            b2 = checkUser.checkUsername(teacher_id)
            if not b2:
                input("您输入的用户名不符合规范,请重新输入...")
                break
            # 遍历列表,看是用户名是否重复
            for t in teacherList:
                if t.teacher_id == teacher_id:
                    input("您的用户名与别人重复,请重新输入!")
                    b1 = False
                    break
            if b1 == True:
                teacher_password = input("请输入您的密码:")

                # 检查密码是否符合规范
                b3 = checkUser.checkPassword(teacher_password)
                if not b3 and b2:
                    input("您输入的密码不符合规范,请重新输入...")
                    break
                else:
                    teacher_name = input("请输入您的姓名:")
                    teacher_age = input("请输入您的年龄:")
                    teacher_sex = input("请输入您的性别:")
                    teacher_adderss = input("请输入您的家庭地址:")
                    tercher_major = input("请输入您教的科目:")
                    # 输入验证码
                    code = verificationCode.verificationCode()
                    inputCode = input("请输入验证码:")
                    if code.upper() == inputCode.upper():
                        # 创建教师实例
                        t = Teacher.Teacher(teacher_id, teacher_password, teacher_name, teacher_age, teacher_sex, teacher_adderss,tercher_major)
                        # 将老师的基本信息添加进列表
                        teacherList.append(t)
                        b2 = Io.TeacherIo().wirite_teacher(teacherList)
                        if b2 == True:
                            input("恭喜您,注册成功!")
                            break
                    else:
                        input("验证码输入错误,请重新输入!")



