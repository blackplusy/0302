#coding=utf-8
#find和index
a='c'
str1='aabbcc'
print(str1.find(a))
a='d'
print(str1.find(a))
#index
a='b'
print(str1.index(a))
a='d'
#print(str1.index(a))
#isalpha()和isdigit()
a='simida'
print(a.isalpha())
a='simida1'
print(a.isalpha())
a='123'
print(a.isdigit())
a='123a'
print(a.isdigit())
#upper()和lower()
name='Apple'
print(name.upper())
print(name.lower())
#startswith()和endswith()
a='aabbcc'
print(a.startswith('a'))
print(a.startswith('b'))
print(a.endswith('c'))
#count、replace、split
name='heygorgaga'
print(name.count('a'))
print(name.replace('a','simida'))
name='1,2,3,4'
b=name.split(',')
print(b)

#引号
print("im your baba!")
print('im your papa!')
print('''我是你爹地！''')

print("i'm your baba!!!")
print('i\'m your baba!!!')

'''
这段代码是:
'''
print('我是小明')
print('我要上学')
print(
'''
我是小军
我不去上学
'''
    )













