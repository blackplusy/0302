#coding=utf-8
class student:
    def __init__(self,name):
        self.name=name
    def info(self):
        print('你的名字是%s'% self.name)

def studentinfo(s):
    s.info()

heygor=student('ladygaga')
#heygor是student类的实例化对象
#对象实例化之后可以调用类的方法
# heygor.info()
studentinfo(heygor)
#studentinfo括号中传入的heygor是一个实例化的对象，可以调用类的方法
# 注意：函数传参可以传入常规函数，也可以传入对象

