#coding=utf-8
#直接访问
l1=['李元芳','李白','钟馗']
print(l1)
#遍历访问
for i in l1:
    print(i)
#成员访问
if '张小敬' in l1:
    print('长安十二时辰')
else:
    print('不在里面')
#列表的索引和切片
l1=['张飞','马超','关羽','黄忠','云云']
print(l1[0])
print(l1[-2])
#print(l1[5])
print(l1[2:])
print(l1[2:3])

#列表的拼接
l1=[1,2,3]
l2=['hello','memeda!']
print(l1+l2)

#列表的更新
l=[1,2,3]
print(l)
l[2]='刘岩'
print(l)
l[-1]='柳岩'
print(l)

#列表的删除
l=[1,2,3]
print(l)
del l[2]
print(l)
del l
print(l)
















