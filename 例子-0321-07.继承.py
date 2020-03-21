#coding=utf-8
# 单继承
# class dog:
#     def __init__(self,name,color='black'):
#         self.name=name
#         self.color=color
#     def run(self):
#         print('狗富贵！互相旺！')
# class taidi(dog):
#     def setname(self,name):
#         self.name=name
#     def eat(self):
#         print('im eating!')
# gou=taidi('big tai tan')
# print('狗的名字%s'%gou.name)
# gou.eat()
# gou.setname('2ha')
# print('旺财的新名字:%s'% gou.name)
# gou.run()
#多继承
# class a:
#     def printa(self):
#         print('---a---')
# class b:
#     def printb(self):
#         print('---b---')
# class c(a,b):
#     def printc(self):
#         print('---c---')
# c1=c()
# c1.printa()
# c1.printb()
# c1.printc()
#父类重写
class dog:
    def sayhi(self):
        print('aowu!!!!!!')

class fadou(dog):
    def sayhi(self):
        print('kouniqiwa!')
dog1=fadou()
dog1.sayhi()
