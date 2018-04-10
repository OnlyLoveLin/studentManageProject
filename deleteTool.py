# 这是一个删除文件

# 导入需要的模块
import Io

# 定义一个查询学生基本信息主界面
def deleteMainMenu():
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.按照学生的编号删除")
        print("\t\t2.按照学生的名字删除")
        print("\t\t3.按照学生的班级删除")
        print("\t\t4.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 按照学生的编号删除
            stuDeleteIdBaseMessage()

        elif c == '2':  # 按照学生的名字删除
            stuDeleteNameBaseMessage()

        elif c == '3':  # 按照学生的班级删除
            stuDeleteClassBaseMessage()

        elif c == '4':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")


# 定义一个从编号删除学生基本信息的函数
def stuDeleteIdBaseMessage():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 从键盘读取信息
    stuId = input("请输入你想要删除的学生编号:")
    if len(stuList) > 0:
        # 遍历列表
        for s in stuList:
            if s.stu_id == stuId:
                stuList.remove(s)
                b = Io.StudentIo().wirite_student(stuList)
                break
        else:
            print("没有此学生")
        if b == True:
            print("删除完成,当前列表还剩:")
            # 变量stu列表
            for s1 in stuList:
                print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                      % (s1.stu_id, s1.stu_name, s1.stu_age, s1.stu_sex, s1.stu_address, s1.stu_class))


# 定义一个从名字删除学生基本信息的函数
def stuDeleteNameBaseMessage():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 创建一个新的列表存储名字重复的学生
    stu = stuList.copy()
    # 从键盘读取信息
    stuName = input("请输入你想要删除的学生名字:")
    if len(stu) > 0:
        # 遍历列表
        for s in stu:
            if s.stu_name == stuName:
                stuList.remove(s)
                b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("删除完成,当前列表还剩:")
        # 变量stu列表
        for s1 in stuList:
            print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                  % (s1.stu_id, s1.stu_name, s1.stu_age, s1.stu_sex, s1.stu_address, s1.stu_class))

    else:
        print("没有此学生!")

# 定义一个从班级删除学生基本信息的函数
def stuDeleteClassBaseMessage():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 创建一个新的列表复制读入的列表
    stu = stuList.copy()
    # 从键盘读取信息
    stuClass = input("请输入你想要删除的班级:")
    if len(stu) > 0:
        # 遍历列表
        for s in stu:
            if s.stu_class == stuClass:
                stuList.remove(s)
                b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("删除完成,当前列表还剩:")
        # 变量stu列表
        for s1 in stuList:
            print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                  % (s1.stu_id, s1.stu_name, s1.stu_age, s1.stu_sex, s1.stu_address, s1.stu_class))
            Io.StudentIo().wirite_student(stuList)
    else:
        print("没有此班级!")

# 定义一个删除学生成绩主界面
def deleteMainGradeMenu():
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.按照学生的编号删除")
        print("\t\t2.按照学生的名字删除")
        print("\t\t3.按照学生的班级删除")
        print("\t\t4.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 按照学生的编号删除
            deleteGradeId()

        elif c == '2':  # 按照学生的名字删除
            deleteGradeName()

        elif c == '3':  # 按照学生的班级删除
            deleteGradeLesson()

        elif c == '4':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# 定义一个按学生编号删除的函数
def deleteGradeId():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 定义一个布尔型变量
    b = False
    # 复制列表
    gList = gradeList.copy()
    # 从键盘读取数据
    stu_id = input("请输入您要删除的学生编号:")
    if len(gList) > 0:
        # 遍历列表
        for g in gList:
            if g.stuId == stu_id:
                gradeList.remove(g)
                b = Io.GradeIo().wirite_grade(gradeList)
    if b == True:
        print("删除完成,当前列表还剩:")
        # 变量stu列表
        for g1 in gradeList:
            print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (g1.stuId,g1.stuLesson,g1.stuName, g1.stuMajor, g1.stuGrade))
            Io.GradeIo().wirite_grade(gradeList)
    else:
        print("没有此学生!")

# 定义一个按学生姓名删除的函数
def deleteGradeName():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 定义一个布尔型变量
    b = False
    # 复制列表
    gList = gradeList.copy()
    # 从键盘读取数据
    stu_name = input("请输入您要删除的学生姓名:")
    if len(gList) > 0:
        # 遍历列表
        for g in gList:
            if g.stuName == stu_name:
                gradeList.remove(g)
                b = Io.GradeIo().wirite_grade(gradeList)
    if b == True:
        print("删除完成,当前列表还剩:")
        # 变量stu列表
        for g1 in gradeList:
            print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (g1.stuId,g1.stuLesson,g1.stuName, g1.stuMajor, g1.stuGrade))
            Io.GradeIo().wirite_grade(gradeList)
    else:
        print("没有此学生!")

# 定义一个按学生编号班级的函数
def deleteGradeLesson():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 定义一个布尔型变量
    b = False
    # 复制列表
    gList = gradeList.copy()
    # 从键盘读取数据
    stu_lesson = input("请输入您要删除的学生班级:")
    if len(gList) > 0:
        # 遍历列表
        for g in gList:
            if g.stuLesson == stu_lesson:
                gradeList.remove(g)
                b = Io.GradeIo().wirite_grade(gradeList)
    if b == True:
        print("删除完成,当前列表还剩:")
        # 变量stu列表
        for g1 in gradeList:
            print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (g1.stuId,g1.stuLesson,g1.stuName, g1.stuMajor, g1.stuGrade))
            Io.GradeIo().wirite_grade(gradeList)
    else:
        print("没有此学生!")
