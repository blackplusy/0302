#coding=utf-8
#栈的方式访问列表
l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(6)
print(l)
l.append(7)
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
#获取列表的索引
l=[6,5,4,3,2,1]
print(l.index(3))
print(l.index(1))
#枚举
l=['a','b','c']
for index,value in enumerate(l):
    print('索引是'+str(index)+',值是:'+str(value))

#排序
print('*'*10)
l=[1,2,4,3]
print(l)
l.reverse()
print(l)

l=[1,3,5,2,4,6]
l.sort()
print(l)
l.reverse()
print(l)

l=[1,3,5,2,4,6]
print(l)
l.sort(reverse=True)
print(l)


#insert
l=['a','b','c']
print(l)
l.insert(1,'d')
print(l)
l.insert(-1,'aaa')
print(l)
#extend
l=[1,2,3,4]
l.extend('a')
print(l)
l.extend([1,2,3])
print(l)





















