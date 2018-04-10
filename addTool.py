# 这是一个添加文件

# 导入需要的模块
import Io

# 导入自定义模块
import Student
import Lesson
import StuGrade


# 定义一个添加学生信息的函数
def addStudent():
    print("\t欢迎来到添加学生基本信息模块")
    # stu_id,stu_name,stu_age,stu_sex,stu_address
    try:
        stuList = Io.StudentIo().read_student()
    except:
        stuList = []
    stuId = input("请输入学生编号:")
    # 判断学生编号是否重复
    for s1 in stuList:
        if stuId == s1.stu_id:
            print("您输入编号已经存在!请重新输入...")
            return
    stuName = input("请输入学生姓名:")
    stuAge = input("请输入学生年龄:")
    stuSex = input("请输入学生性别:")
    stuAddress = input("请输入学生的家庭住址:")
    stuClass = input("请输入学生的班级:")
    # 创建学生对象
    s = Student.Student(stuId,stuName,stuAge,stuSex,stuAddress,stuClass)
    # 将学生对象添加进列表
    stuList.append(s)
    # 将列表写入文件
    b = Io.StudentIo().wirite_student(stuList)
    if b == True:
        print("添加成功!")
    else:
        print("添加失败!")


# 定义一个添加课程表的函数,t为当前登录教师对象
def lessonList(t):
    try:
        lessonList = Io.LessonIo().read_lesson()
    except:
        lessonList = []
    print("您所教的科目是:%s" %t.teacher_major)
    lessonMajor = t.teacher_major
    lessonTeacher = t.teacher_name
    # 从键盘输入所交课程最多人数
    lessonNum = input("请输入您所教课程最多人数:")
    # 从键盘读取您要授课的时间
    lessonTime = input("请输入您要授课的时间:")
    # 创建一个课程实例
    l = Lesson.Lesson(lessonMajor,lessonTeacher,lessonNum,lessonTime)
    print("您添加的课程为:%s--人数为:%s--时间为:%s" %(l.lesson_name,l.lesson_num,l.lesson_time))
    # 将添加的信息写入日志中
    log = "%s老师添加课程:%s--人数为:%s--时间为:%s" %(t.teacher_name,l.lesson_name,l.lesson_num,l.lesson_time)+"\n"
    # 将日志写入
    Io.Log().wirite_log(log)
    # 将课程实例写入课程列表中
    lessonList.append(l)
    # 将课程写入文件中
    b = Io.LessonIo().wirite_lesson(lessonList)
    if b == True:
        print("添加课程表成功!")
    else:
        print("添加课程失败!")


# 定义一个添加学生成绩的函数,t为当前登录教师对象
def addStuGrade(t):
    # 获取学生列表
    try:
        stuList = Io.StudentIo().read_student()
    except:
        return print("请先添加学生!")
    try:
        gradeList = Io.GradeIo().read_lesson()
    except:
        gradeList = []

    # 定义一个布尔型变量
    b1 = True
    # 遍历获取学生选择的科目
    for s in stuList:
        major = s.stu_lesson
        for m in major:
            # 判断老师教的科目是否在学生选择的科目列表中
            if t.teacher_major == m.lesson_name:
                # 遍历列表判断学生成绩是否已经录入过
                for g1 in gradeList:
                    if g1.stuId == s.stu_id and t.teacher_major == g1.stuMajor:
                        input("%s学生的%s成绩已经存在,请不要重复添加!" % (g1.stuName, t.teacher_major))
                        break
                else:
                    stuId = s.stu_id
                    stuGrade = input("%s学生的%s成绩为:\n" % (s.stu_name, m.lesson_name))
                    stuName = s.stu_name
                    stuLesson = s.stu_class
                    stuMajor = m.lesson_name
                    # 创建学生分数实例
                    stu = StuGrade.StuGrade(stuId, stuName, stuLesson, stuGrade, stuMajor)
                    gradeList.append(stu)
                    b = Io.GradeIo().wirite_grade(gradeList)
                    if b == True:
                        input("成绩录入成功!按任意键继续...")
    else:
        print("暂无学生成绩可录!")
