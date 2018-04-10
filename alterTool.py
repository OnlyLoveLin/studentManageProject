# 这是一个修改信息的文件

# 导入需要的模块
import Io


# 查找需要修改的学生编号
def findAlterStu():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 从键盘读取信息
    stuId = input("请输入你想要修改的学生编号:")
    if len(stuList) > 0:
        # 遍历列表
        for s in stuList:
            if s.stu_id == stuId:
                alterMainMenu(s)
                break
        else:
            print("没有此学生!")


# 定义一个修改学生基本信息主界面
def alterMainMenu(s):
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.修改学生%s的名字" % s.stu_name)
        print("\t\t2.修改学生%s的年龄" % s.stu_name)
        print("\t\t3.修改学生%s的性别" % s.stu_name)
        print("\t\t4.修改学生%s的家庭住址" % s.stu_name)
        print("\t\t5.修改学生%s的班级" % s.stu_name)
        print("\t\t6.修改学生%s的所有信息" % s.stu_name)
        print("\t\t7.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 修改学生的名字
            stuAlterNameBaseMessage(s)

        elif c == '2':  # 修改学生的年龄
            stuAlterAgeBaseMessage(s)

        elif c == '3':  # 修改学生的性别
            stuAlterSexBaseMessage(s)

        elif c == '4':  # 修改学生的家庭住址
            stuAlterAddresssBaseMessage(s)

        elif c == '5':  # 修改学生的班级
            stuAlterClassBaseMessage(s)

        elif c == '6':  # 修改学生的所有信息
            stuAlterAllBaseMessage(s)

        elif c == '7':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")


# 定义一个函数修改学生的姓名
def stuAlterNameBaseMessage(s):
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 遍历列表
    for s1 in stuList:
        if s1.stu_id == s.stu_id:
            stuName = input("请输入学生新的姓名:")
            s1.stu_name = stuName
            b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("修改名字成功!")
        for s2 in stuList:
            if s2.stu_id == s.stu_id:
                print("当前学生信息为:")
                print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s"\
                      % (s2.stu_id, s2.stu_name, s2.stu_age, s2.stu_sex, s2.stu_address, s2.stu_class))
    else:
        print("修改名字失败!")


# 定义一个函数修改学生的年龄
def stuAlterAgeBaseMessage(s):
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 遍历列表
    for s1 in stuList:
        if s1.stu_id == s.stu_id:
            stuAge = input("请输入学生新的年龄:")
            s1.stu_age = stuAge
            b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("修改年龄成功!")
        for s2 in stuList:
            if s2.stu_id == s.stu_id:
                print("当前学生信息为:")
                print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                      % (s2.stu_id, s2.stu_name, s2.stu_age, s2.stu_sex, s2.stu_address, s2.stu_class))
    else:
        print("修改年龄失败!")


# 定义一个函数修改学生的性别
def stuAlterSexBaseMessage(s):
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 遍历列表
    for s1 in stuList:
        if s1.stu_id == s.stu_id:
            stuSex = input("请输入学生新的性别:")
            s1.stu_sex = stuSex
            b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("修改性别成功!")
        for s2 in stuList:
            if s2.stu_id == s.stu_id:
                print("当前学生信息为:")
                print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                      % (s2.stu_id, s2.stu_name, s2.stu_age, s2.stu_sex, s2.stu_address, s2.stu_class))
    else:
        print("修改性别失败!")


# 定义一个函数修改学生的家庭住址
def stuAlterAddresssBaseMessage(s):
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 遍历列表
    for s1 in stuList:
        if s1.stu_id == s.stu_id:
            stuAddress = input("请输入学生新的家庭住址:")
            s1.stu_address = stuAddress
            b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("修改家庭住址成功!")
        for s2 in stuList:
            if s2.stu_id == s.stu_id:
                print("当前学生信息为:")
                print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                      % (s2.stu_id, s2.stu_name, s2.stu_age, s2.stu_sex, s2.stu_address, s2.stu_class))
    else:
        print("修改家庭住址失败!")


# 定义一个函数修改学生的班级
def stuAlterClassBaseMessage(s):
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 遍历列表
    for s1 in stuList:
        if s1.stu_id == s.stu_id:
            stuClass = input("请输入学生新的班级:")
            s1.stu_class = stuClass
            b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("修改班级成功!")
        for s2 in stuList:
            if s2.stu_id == s.stu_id:
                print("当前学生信息为:")
                print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                      % (s2.stu_id, s2.stu_name, s2.stu_age, s2.stu_sex, s2.stu_address, s2.stu_class))
    else:
        print("修改班级失败!")


# 修改该学生所有的信息
def stuAlterAllBaseMessage(s):
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 遍历列表
    for s1 in stuList:
        if s1.stu_id == s.stu_id:
            stuName = input("请输入学生新的姓名:")
            stuAge = input("请输入学生新的年龄:")
            stuSex = input("请输入学生新的性别:")
            stuAddress = input("请输入学生新的地址:")
            stuClass = input("请输入学生新的班级:")
            s1.stu_name = stuName
            s1.stu_age = stuAge
            s1.stu_sex = stuSex
            s1.stu_address = stuAddress
            s1.stu_class = stuClass
            b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("修改班级成功!")
        for s2 in stuList:
            if s2.stu_id == s.stu_id:
                print("当前学生信息为:")
                print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                      % (s2.stu_id, s2.stu_name, s2.stu_age, s2.stu_sex, s2.stu_address, s2.stu_class))


# 定义一个函数修改学生的成绩,t为当前登录教师对象
def alterStuGrade(t):
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    stu_id = input("请输入您要修改学生的编号:")
    # 定义一个布尔型变量
    b = False
    # 遍历列表
    for g in gradeList:
        if stu_id == g.stuId and t.teacher_major == g.stuMajor:
            stu_grade = input("请重新输入%s同学的%s成绩:" %(g.stuName,g.stuMajor))
            g.stuGrade = stu_grade
            b = Io.GradeIo().wirite_grade(gradeList)
            break
    if b == True:
        for g1 in gradeList:
            if g1.stuId == stu_id:
                print("修改成绩成功!目前成绩为:")
                print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (g1.stuId, g1.stuLesson, g1.stuName, g1.stuMajor, g1.stuGrade))
    else:
        print("无此编号!")
