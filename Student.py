# 这是一个学生类
class Student:
    # 初始化属性
    def __init__(self,stu_id,stu_name,stu_age,stu_sex,stu_address,stu_class,stu_lesson = None):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_age = stu_age
        self.stu_sex = stu_sex
        self.stu_address = stu_address
        self.stu_class = stu_class
        if stu_lesson == None:
            stu_lesson = []
        self.stu_lesson = stu_lesson

    # 定义一个添加课程的函数
    def addLesson(self,stu_lesson):
        self.stu_lesson.append(stu_lesson)


