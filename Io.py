# 该文件主要执行io操作

# 导入需要的模块
import os
import pickle

# 定义一个教师io类
class TeacherIo:
    # 定义一个将老师基本信息写入文件的函数
    def wirite_teacher(self,teacherList):
        # 建立待读取的路径
        files = "package/老师基本信息.txt"
        # 获取父级路径
        parent_dir = os.path.dirname(files)
        # 判断父级目录是否存在
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        # 打开文件
        f = open(files,"wb")
        # 写入文件
        pickle.dump(teacherList,f)
        # 关闭资源
        f.close()
        return  True

    # 定义一个将老师基本信息从文件读取出来的函数
    def read_teacher(self):
        # 建立待读取的路径
        files = "package/老师基本信息.txt"
        # 打开文件
        f = open(files,"rb")
        # 读取文件
        teacherList = pickle.load(f)
        f.close()
        return teacherList

# ----------------------------------------------------------------------------------------------------------
# 以下是学生io

# 定义一个学生io类
class StudentIo:
    # 定义一个将老师基本信息写入文件的函数
    def wirite_student(self,studentList):
        # 建立待读取的路径
        files = "package/学生基本信息.txt"
        # 获取父级路径
        parent_dir = os.path.dirname(files)
        # 判断父级目录是否存在
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        # 打开文件
        f = open(files,"wb")
        # 写入文件
        pickle.dump(studentList,f)
        # 关闭资源
        f.close()
        return  True

    # 定义一个将学生基本信息从文件读取出来的函数
    def read_student(self):
        # 建立待读取的路径
        files = "package/学生基本信息.txt"
        # 打开文件
        f = open(files,"rb")
        # 读取文件
        studentList = pickle.load(f)
        f.close()
        return studentList

# ----------------------------------------------------------------------------------------------------------
# 以下是课程Io

# 定义一个课程io类
class LessonIo:
    # 定义一个将课程基本信息写入文件的函数
    def wirite_lesson(self,lessonList):
        # 建立待读取的路径
        files = "package/课程基本信息.txt"
        # 获取父级路径
        parent_dir = os.path.dirname(files)
        # 判断父级目录是否存在
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        # 打开文件
        f = open(files,"wb")
        # 写入文件
        pickle.dump(lessonList,f)
        # 关闭资源
        f.close()
        return  True

    # 定义一个将课程基本信息从文件读取出来的函数
    def read_lesson(self):
        # 建立待读取的路径
        files = "package/课程基本信息.txt"
        # 打开文件
        f = open(files,"rb")
        # 读取文件
        lessonList = pickle.load(f)
        f.close()
        return lessonList

# ----------------------------------------------------------------------------------------------------------

# 定义一个成绩io类
class GradeIo:
    # 定义一个将成绩基本信息写入文件的函数
    def wirite_grade(self, gradeList):
        # 建立待读取的路径
        files = "package/学生成绩信息.txt"
        # 获取父级路径
        parent_dir = os.path.dirname(files)
        # 判断父级目录是否存在
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        # 打开文件
        f = open(files, "wb")
        # 写入文件
        pickle.dump(gradeList, f)
        # 关闭资源
        f.close()
        return True

    # 定义一个将成绩基本信息从文件读取出来的函数
    def read_lesson(self):
        # 建立待读取的路径
        files = "package/学生成绩信息.txt"
        # 打开文件
        f = open(files, "rb")
        # 读取文件
        gradeList = pickle.load(f)
        f.close()
        return gradeList

# ----------------------------------------------------------------------------------------------------------
# 定义一个日志类

class Log:
    def wirite_log(self, log):
        # 建立待读取的路径
        files = "package/日志信息.txt"
        # 获取父级路径
        parent_dir = os.path.dirname(files)
        # 判断父级目录是否存在
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        # 打开文件
        f = open(files, "a",encoding = "UTF-8")
        # 写入文件
        f.write(log)
        # 关闭资源
        f.close()

