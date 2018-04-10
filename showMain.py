# 这是一个展示主界面的函数

# 导入需要的模块
import time
import sys

# 导入需要的自定义模块
import regist       # 教师注册模块
import login        # 教师登录模块
import addTool      # 添加模块
import referTool    # 查看模块
import deleteTool   # 删除模块
import alterTool    # 修改模块
import choiceLesson # 选课模块
import soreFile     # 排序模块

# 主界面,选择客户端登录
def choiceClient():
    while True:
        print("------------------------------------")
        print("\t学生管理系统")
        print("\t\t1.教师登录")
        print("\t\t2.学生登录")
        print("\t\t3.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 教师登录
            teacherClient()

        elif c == '2':  # 教师登录
            studentClient()

        elif c == '3':  # 退出
            print("系统将在3秒后退出!")
            time.sleep(3)
            sys.exit(0)
        else:
            input("没有这个选项,请重新输入!")

# ----------------------------------------------------------------------------------------------------------
# 以下是客户端界面

# 定义一个教师端的界面
def teacherClient():
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.注册")
        print("\t\t2.登录")
        print("\t\t3.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 注册
            regist.regist()

        elif c == '2':  # 登录
            login.teacherLogin()

        elif c == '3':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# 定义一个学生端的界面
def studentClient():
    while True:
        print("------------------------------------")
        print("\t学生客户端")
        print("\t\t1.登录")
        print("\t\t2.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 登录
            login.stuLogin()

        elif c == '2':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# ----------------------------------------------------------------------------------------------------------
# 以下是操作界面

# 定义一个教师操作主界面,t为当前登录教师对象
def teacherShowMenu(t):
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.添加操作")
        print("\t\t2.查询操作")
        print("\t\t3.删除操作")
        print("\t\t4.修改操作")
        print("\t\t5.查看排行榜")
        print("\t\t6.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 添加操作,t为当前登录教师对象
            teacherAddMenu(t)

        elif c == '2':  # 查询操作
            teacherReferMenu()

        elif c == '3':  # 删除操作
            teacherDelectMenu()

        elif c == '4':  # 修改操作,t为当前登录教师对象
            teacherAlterMenu(t)

        elif c == '5':  # 查看排行榜
            teacherSortMenu()

        elif c == '6':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")


# 定义一个学生端的界面,s为当前登录学生对象
def studentShowMenu(s):
    while True:
        print("------------------------------------")
        print("\t学生客户端")
        print("\t\t1.选课")
        print("\t\t2.查询自己基本信息")
        print("\t\t3.查询自己成绩信息")
        print("\t\t4.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 选课,s为当前登录学生对象
            choiceLesson.choiceLesson(s)

        elif c == '2':  # 查询自己基本信息,s为当前登录学生对象
            referTool.stuBaseMessage(s)

        elif c == '3':  # 查询自己成绩信息,s为当前登录学生对象
            referTool.referStuGrade(s)

        elif c == '4':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# ----------------------------------------------------------------------------------------------------------
# 以下是教师操作界面

# 定义一个添加操作界面,t为当前登录教师对象
def teacherAddMenu(t):
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.添加学生的基本信息")
        print("\t\t2.添加课程表")
        print("\t\t3.添加学生成绩信息")
        print("\t\t4.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 添加学生的基本信息
            addTool.addStudent()

        elif c == '2':  # 添加课程表,t为当前登录教师对象
            addTool.lessonList(t)

        elif c == '3':  # 添加学生成绩信息,t为当前登录教师对象
           addTool.addStuGrade(t)

        elif c == '4':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# 定义一个查询操作界面
def teacherReferMenu():
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.查询学生的基本信息")
        print("\t\t2.查询学生成绩信息")
        print("\t\t3.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 查询学生的基本信息
           referTool.referMainMenu()

        elif c == '2':  # 查询学生成绩信息
            referTool.referGradeMainMenu()

        elif c == '3':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# 定义一个删除操作界面
def teacherDelectMenu():
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.删除学生的基本信息")
        print("\t\t2.删除学生成绩信息")
        print("\t\t3.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 删除学生的基本信息
            deleteTool.deleteMainMenu()

        elif c == '2':  # 删除学生成绩信息
            deleteTool.deleteMainGradeMenu()

        elif c == '3':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# 定义一个修改操作界面,t为当前登录教师对象
def teacherAlterMenu(t):
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.修改学生的基本信息")
        print("\t\t2.修改学生成绩信息")
        print("\t\t3.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 修改学生的基本信息
            alterTool.findAlterStu()

        elif c == '2':  # 修改学生成绩信息,t为当前登录教师对象
            alterTool.alterStuGrade(t)

        elif c == '3':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")

# 定义一个排序操作界面
def teacherSortMenu():
    while True:
        print("------------------------------------")
        print("\t教师客户端")
        print("\t\t1.查看学生科目成绩排行")
        print("\t\t2.查看学生总成绩排行")
        print("\t\t3.退出")
        print("------------------------------------")
        c = input("请输入您的选项:")
        if c == '1':  # 查看学生科目成绩排行
            soreFile.sortMajor()

        elif c == '2':  # 查看学生总成绩排行
            soreFile.sortAllGrade()

        elif c == '3':  # 退出
            break

        else:
            input("没有这个选项,请重新输入!")
