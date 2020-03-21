#coding=utf-8
class student:
    def study(self):
        print('im study!')
    def play(self):
        print('im play ball')

boy=student()
#产生一个studeng对象，通过boy实例对象来访问属性和方法
boy.age=20
boy.favor='baseball'
#给对象添加属性，注意:后面如果再次出现标识堆属性的修改
boy.study()
#通过实例对象访问类的方法
print(boy.age)
print(boy.favor)
#通过实例对象访问实例属性


