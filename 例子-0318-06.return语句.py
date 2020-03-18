#coding=utf-8
#一个返回值

def sum(a,b):
    jisuan=a+b
    return jisuan

a=sum(20,30)
print(a)

#多个返回值
def ret(a,b):
    a*=10
    b*=100
    return a,b
num=ret(5,7)
print(num)
print(type(num))

num1,num2=ret(4,100)
print(num1)
print(num2)
print(type(num1))
