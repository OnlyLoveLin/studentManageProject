# 这是一个选课文件

# 导入需要的自定义模块
import Io
import Student

# 定义一个选课函数,s为当前登录学生对象
def choiceLesson(s):
    # 读取课程列表
    try:
        lessonList = Io.LessonIo().read_lesson()
    except:
        lessonList = []
    # 遍历课程列表
    for l1 in lessonList:
        print("课程名称:%s--课程老师:%s--课程余量:%s--课程时间:%s" \
              %(l1.lesson_name,l1.lesson_teacher,l1.lesson_num,l1.lesson_time))
    # 读取学生列表
    stuList = Io.StudentIo().read_student()
    # 获取学生已经选过的课程
    lessonOldManage = s.stu_lesson
    # 定义布尔型变量
    b1 = False
    b2 = False
    # 从键盘读入学生选择的课程和时间
    lessonName = input("请选择你要选择的课程:")
    lessonTime = input("请选择你的上课时间:")
    for lo in lessonOldManage:
        # 判断学生是否选过此课程
        if lessonName == lo.lesson_name and lessonTime == lo.lesson_time:
            input("您已经选过此课,请不要重复选取!")
            return
    # 遍历列表
    for l in lessonList:
        # 选择课程
        if lessonName == l.lesson_name and lessonTime == l.lesson_time:
            b1 = True
            l.lesson_num = int(l.lesson_num)
            # 判断课程是否还有余量
            if l.lesson_num > 0:
                b2 = True
                l.lesson_num -= 1
                #将课程实例写入学生课程属性中
                Io.LessonIo().wirite_lesson(lessonList)
                Student.Student.addLesson(s,l)
                # 遍历学生列表
                for s1 in stuList:
                    if s.stu_id == s1.stu_id:
                        # 更新学生的信息
                        s1.stu_lesson =s.stu_lesson
                        b = Io.StudentIo().wirite_student(stuList)
                        if b == True:
                            print("恭喜您,选课成功!")
                            # 将选课信息写入日志中
                            log = "%s同学选择课程为:%s--时间:%s--当前余量为%s"\
                                  %(s.stu_name,l.lesson_name,l.lesson_time,l.lesson_num) + "\n"
                            Io.Log().wirite_log(log)
                            lessonManage = s.stu_lesson
                            for lm in lessonManage:
                                print("您选择的课程为:%s--时间:%s.请按时上课!"%(lm.lesson_name,lm.lesson_time))
                            return
                        else:
                            print("选课失败!")
    if b1 == False:
        print("您输入的课程或时间不存在,请重新输入!")
    if b1 == True and b2 == False:
        print("您选择的课程余量不够,请选择其他课程!")
