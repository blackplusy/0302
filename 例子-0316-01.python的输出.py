#coding=utf-8
#coding=utf-8 设置字符集位utf-8
#字符集相当于翻译官，解析不同语言用于显示
#中文字符集 GBK2312
#1.直接输出
#直接输出是通过print()函数进行打印，把括号中内容显示在屏幕上
#屏幕上输出翻滚吧牛宝宝
print('翻滚吧牛宝宝！')
print(123)
#2.变量输出
#变量可以理解为容器，容器的值是不固定的，设置什么就保存什么
#变量的名字是name，变量的值是python
name='python'
#输出变量name的值
print(name)
#.变量操作输出
a=100
b=30
print(a+b)
a='heygor is '
b='no.1'
print(a+b)
#3.函数输出
#输出函数处理过的值
# abs()  绝对值
# len()  字符串的长度(元素的个数)
print(abs(-20))
name='heygorgaga'
print(len(name))
#4.格式化输出
#  %s 输出字符串
#  %d 输出整型
#如果语句中只传入一个变量，不用加括号，如果多个需要加括号
name='python'
no=1
print('%s is no.%d'%(name,no))

name='heygor'
print('%s is so so handsome!!!'% name)

#print('%d is good'% name)







