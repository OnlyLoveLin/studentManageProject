# 这是一个学生成绩排行文件

# 导入自定义模块
import Io

# 定义一个按科目排序的函数
def sortMajor():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 从键盘读取输入科目
    major = input("请输入您想要查看的科目:")
    # 创建一个新的列表用来存储科目此成绩
    sortList = []
    # 定义一个布尔型变量
    b = False
    # 遍历成绩列表
    for m in gradeList:
        if m.stuMajor == major:
            sortList.append(m)
            b = True

    if b == False:
        print("没有此科目!")

    # 对对象进行排序
    for x in range(0,len(sortList) - 1):
        for y in range(0, len(sortList) - x - 1):
            if sortList[y].stuGrade < sortList[y+1].stuGrade:
                c = sortList[y]
                sortList[y]= sortList[y+1]
                sortList[y+1] = c

    for s in sortList:
        print("编号:%s--班级:%s--%s学生的%s成绩为:%s" % (s.stuId, s.stuLesson, s.stuName, s.stuMajor, s.stuGrade))

# 定义一个总成绩排序
def sortAllGrade():
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        return print("请先添加成绩!")
    # 创建一个新的列表存放总成绩
    sortAllList = []
    # 创建一个列表存放学生姓名
    sortAllName = []
    # 遍历列表
    for g1 in gradeList:
        # 如果是第一次添加,就直接添加进去
        if len(sortAllName) == 0:
            sortAllName.append(g1.stuName)
        else:
            # 如果不是第一次添加,就遍历看元素是否与gradeList列表元素重复
            for m in sortAllName:
                if m == g1.stuName:
                    break
            else:
                sortAllName.append(g1.stuName)
    # 遍历存放学生姓名的列表
    for n in sortAllName:
        stu_grade = 0
        # 遍历成绩列表
        for g in gradeList:
            g.stuGrade = int(g.stuGrade)
            if n == g.stuName:
                    stu_grade += g.stuGrade
        # 创建个字典存储当前学生的总成绩
        sortAllDict = {}
        sortAllDict["name"] = n
        sortAllDict["allGrade"] = stu_grade
        # 把学生成绩添加进列表
        sortAllList.append(sortAllDict)
    # 进行排序
    for x in range(0,len(sortAllList)-1):
        for y in range(0,len(sortAllList)-x-1):
            if sortAllList[y].get("allGrade") < sortAllList[y+1].get("allGrade"):
                c = sortAllList[y]
                sortAllList[y] = sortAllList[y+1]
                sortAllList[y+1] = c

    print("------------------------------------")
    print("\t总成绩排名")
    sum = 1
    for s in sortAllList:
        print("名次:%s.姓名:%s 总分数:%s" %(sum,s.get("name"),s.get("allGrade") ))
        sum += 1


