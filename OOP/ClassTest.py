class Student():
    #，一个空类，pass代表直接跳过，此处pass必须有
    pass
class PythonStudent():
    #必须赋值
    name=None
    age=None
    course="Python"
    #需要注意
    #1、def doHomeWork的缩进层级
    #2、默认有self参数
    #3、末尾建议使用return
    def doHomeWork(self):
        print(self.name+"在做作业")
        return None

wangli=Student()
#实例化
yueyue=PythonStudent()
print(yueyue.name)
print(yueyue.age)
print(yueyue.course)