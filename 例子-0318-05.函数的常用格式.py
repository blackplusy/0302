#coding=utf-8
#1.无参数，无返回值
def print_name():
    print('我的名字是dingdong！')
print_name()

#2.无参数，有返回值
def sleep():
    return 'im sleeping!!!'
s=sleep()
print(s)

#3.有参数，无返回值
def sub(x,y):
    print('x+y=',x+y)

sub(20,10)
#4.有参数，有返回值
def sub(x,y):
    return x+y
s=sub(5,13)
print(s)

    
