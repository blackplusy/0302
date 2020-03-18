#coding=utf-8
#创建元组
tup=(1)
print(tup)
print(type(tup))

tup1=(2,)
print(tup1)
print(type(tup1))

#元组的访问
tup=(1,2,3,4)
print(tup)

for i in  tup:
    print(i)

if 1 in tup:
    print('1 is here!')

#删除元组
tup=(1,2,3,4)
del tup
#print(tup)
#索引和切片
tup=(1,2,3,4,3,3,3,3,3)
print(tup[0])
print(tup[-2])
print(tup[2:4])
print(tup[2:])
#元组的补充
tup=(1,2,3,4,3,3,3,3,3)
print(len(tup))
print(max(tup))
print(tup.index(3))
print(tup.count(3))








