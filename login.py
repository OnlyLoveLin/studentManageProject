# 这是一个登录文件

# 导入需要的自定义模块
import Io
import showMain
import verificationCode

# 定义一个教师登录函数
def teacherLogin():
    try:
        teacherList = Io.TeacherIo().read_teacher()
    except:
        return print("请先注册用户!")
    # 定义布尔类型
    b = True
    # 提示用户输入用户名
    teacherId = input("请输入您的登录用户名(按r键退出):")
    if teacherId == "r":
        b = False
    if b == True:
        # 提示用户输入密码
        teacherPassword = input("请输入您的登录密码:")
        # 验证验证码
        code = verificationCode.verificationCode()
        inputCode = input("请输入验证码:")
        if code.upper() == inputCode.upper():
            # 遍历列表
            for t in teacherList:
                if t.teacher_id == teacherId and t.teacher_password == teacherPassword:
                    print(t.teacher_name+":")
                    print("\t欢迎来到学生管理系统!")
                    showMain.teacherShowMenu(t)
                    break
            else:
                input("登录失败,按任意键返回...")
        else:
            input("验证码错误,请重新输入!")
    else:
        return showMain.teacherClient()

# -----------------------------------------------------------------------------------------------------------
# 以下是学生端功能

# 定义一个学生登录函数
def stuLogin():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请等待老师添加哟.")
    # 提示学生输入自己的编号:
    stuId = input("请输入您的编号:")
    stuName = input("请输入您的姓名:")
    # 验证验证码
    code = verificationCode.verificationCode()
    inputCode = input("请输入验证码:")
    if code.upper() == inputCode.upper():
        # 遍历列表
        for s in stuList:
            if stuName == s.stu_name and stuId == s.stu_id:
                print("欢迎%s同学!" %s.stu_name)
                showMain.studentShowMenu(s)
                break

        else:
            print("暂无此学生!")
    else:
        input("验证码错误,请重新输入!")
