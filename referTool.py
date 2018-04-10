# 这是一个查询文件

# 导入需要的模块
import Io

# 定义一个查询学生基本信息主界面
def referMainMenu():
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.按照学生的编号查询")
        print("\t\t2.按照学生的名字查询")
        print("\t\t3.按照学生的班级查询")
        print("\t\t4.查询所有学生")
        print("\t\t5.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 按照学生的编号查询
            stuReferIdBaseMessage()

        elif c == '2':  # 按照学生的名字查询
            stuReferNameBaseMessage()

        elif c == '3':  # 按照学生的班级查询
            stuReferClassBaseMessage()

        elif c == '4':  # 查询所有学生
            stuReferBaseMessage()

        elif c == '5':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")


# 定义一个从编号查询学生基本信息的函数
def stuReferIdBaseMessage():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 从键盘读取信息
    stuId = input("请输入你想要查询的学生编号:")
    if len(stuList) > 0:
        # 遍历列表
        for s in stuList:
            if s.stu_id == stuId:
                print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                      %(s.stu_id,s.stu_name,s.stu_age,s.stu_sex,s.stu_address,s.stu_class))
                break
        else:
            print("没有此学生")

# 定义一个从名字查询学生基本信息的函数
def stuReferNameBaseMessage():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 创建一个新的列表存储名字重复的学生
    stu = []
    # 从键盘读取信息
    stuName = input("请输入你想要查询的学生名字:")
    if len(stuList) > 0:
        # 遍历列表
        for s in stuList:
            if s.stu_name == stuName:
                stu.append(s)
                b = True
    if b == True:
        # 变量stu列表
        for s1 in stu:
            print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                  % (s1.stu_id, s1.stu_name, s1.stu_age, s1.stu_sex, s1.stu_address, s1.stu_class))
    else:
        print("没有此学生!")

# 定义一个从班级查询学生基本信息的函数
def stuReferClassBaseMessage():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    # 定义一个布尔型变量
    b = False
    # 创建一个新的列表存储名字重复的学生
    stu = []
    # 从键盘读取信息
    stuClass = input("请输入你想要查询的班级:")
    if len(stuList) > 0:
        # 遍历列表
        for s in stuList:
            if s.stu_class == stuClass:
                stu.append(s)
                b = True
    if b == True:
        # 变量stu列表
        for s1 in stu:
            print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                  % (s1.stu_id, s1.stu_name, s1.stu_age, s1.stu_sex, s1.stu_address, s1.stu_class))
    else:
        print("没有此班级!")

# 定义个函数查询所有学生
def stuReferBaseMessage():
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    if len(stuList) > 0:
        # 遍历列表
        for s in stuList:
            print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                  % (s.stu_id, s.stu_name, s.stu_age, s.stu_sex, s.stu_address, s.stu_class))

# ----------------------------------------------------------------------------------------------------------
# 以下是查看学生成绩

# 定义一个查询学生基本信息主界面
def referGradeMainMenu():
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.按照学生的编号查询")
        print("\t\t2.按照学生的名字查询")
        print("\t\t3.按照学生的班级查询")
        print("\t\t4.查询所有学生")
        print("\t\t5.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 按照学生的编号查询
            stuReferGradeId()

        elif c == '2':  # 按照学生的名字查询
            stuReferGradeName()

        elif c == '3':  # 按照学生的班级查询
            stuReferGradeLesson()

        elif c == '4':  # 查询所有学生成绩
            stuReferGradeAll()

        elif c == '5':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# 定义一个按编号查询学生成绩的函数
def stuReferGradeId():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 定义一个布尔型变量
    b = False
    # 定义个变量存放总分数
    sum = 0
    # 定义个列表存放该编号的成绩
    gList = []
    # 提示用户输入学生编号
    stu_id = input("请输入学生编号:")
    # 遍历列表,查找编号相同的学生
    for g in gradeList:
        if stu_id == g.stuId:
            sum += int(g.stuGrade)
            # 如果存在,就添加进列表
            gList.append(g)
            b = True
    if b == True:
        for g1 in gList:
            print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (g1.stuId,g1.stuLesson,g1.stuName, g1.stuMajor, g1.stuGrade))
        print("总分为:%s" %sum)
    else:
        print("您输入的编号不存在")

# 定义一个按名字查询学生成绩的函数
def stuReferGradeName():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 定义一个布尔型变量
    b = False
    # 定义个列表存放该姓名的成绩
    gList = []
    # 定义个变量存放总分数
    sum = 0
    # 提示用户输入学生姓名
    stu_name = input("请输入学生姓名:")
    # 遍历列表,查找编号相同的学生
    for g in gradeList:
        if stu_name == g.stuName:
            sum += int(g.stuGrade)
            # 如果存在,就添加进列表
            gList.append(g)
            b = True
    if b == True:
        for g1 in gList:
            print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (g1.stuId,g1.stuLesson,g1.stuName, g1.stuMajor, g1.stuGrade))
        print("总分为:%s" % sum)
    else:
        print("您输入的姓名不存在")

# 定义一个按班级查询学生成绩的函数
def stuReferGradeLesson():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 定义一个布尔型变量
    b = False
    # 定义个列表存放该班级的成绩
    gList = []
    # 提示用户输入班级
    stu_lesson = input("请输入班级:")
    # 遍历列表,查找班级相同的学生
    for g in gradeList:
        if stu_lesson == g.stuLesson:
            # 如果存在,就添加进列表
            gList.append(g)
            b = True
    if b == True:
        for g1 in gList:
            print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (g1.stuId,g1.stuLesson,g1.stuName, g1.stuMajor, g1.stuGrade))
    else:
        print("您输入的班级不存在")

# 定义一个查询学生所有成绩的函数
def stuReferGradeAll():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    for g1 in gradeList:
        print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (g1.stuId, g1.stuLesson, g1.stuName, g1.stuMajor, g1.stuGrade))

# ----------------------------------------------------------------------------------------------------------
# 以下是学生端功能

# 查询学生的基本信息,s1为当前登录学生对象
def stuBaseMessage(s1):
    stuList = Io.StudentIo().read_student()
    for s in stuList:
        if s1.stu_id == s.stu_id:
            print("%s学生的基本信息为:" %s.stu_name)
            print("编号:%s--姓名:%s--年龄:%s--性别:%s--家庭住址:%s--班级:%s" \
                  % (s.stu_id, s.stu_name, s.stu_age, s.stu_sex, s.stu_address, s.stu_class))
            break
    else:
        print("请输入正确的编号!")

# 定义一个查看学生成绩的函数,s1为当前登录学生对象
def referStuGrade(s1):
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 定义个变量存放学生的总成绩
    sum = 0
    for g in gradeList:
        if g.stuId == s1.stu_id:
            sum += int(g.stuGrade)
            print("您的%s成绩为:%s" % (g.stuMajor, g.stuGrade))
    print("您的总分为:%s" %sum)

