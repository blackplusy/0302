#coding=utf-8
str1='memeda'
#字符串
for i in str1:
    if i=='m':
        print('m is here')
    print(i)
#列表
l=[1,2,'simida','kouniqiwa']

for a in l:
    print(a)

#函数
#range函数
#range(10)   0-9
#range(1,10) 1-9
print('---------------------')

for i in range(10):
    print(i)

print('---------------------')

for i in range(1,10):
    print(i)


print('---------------------')
for i in range(-5,5):
    if i<0:
        print(-i)
    else:
        print(i)

#补充:打印*
for i in range(5):
    print(i*'*')





