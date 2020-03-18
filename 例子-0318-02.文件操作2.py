#coding=utf-8
file=open('E:\\3.txt','r')
for i in file.readlines():
    #print(i)
    #print(type(i))
    i=i.strip('\n')
    a=i.split(' ')
    #print(a)
    if a[-1]=='110':
        print('110 is here!')
file.close()
#尝试用另外一种方法

