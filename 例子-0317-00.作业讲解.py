#coding=utf-8
'''
for i in range(-3,4):
    if i<0:
        a=-i
    else:
        a=i
    print(' '*a+'*'*(7-a*2))
'''
'''
n=7
e=n//2  #3
for i in range(-e,n-e):
    a=-i if i<0 else i
    #print(a)
    print(' '*(e-a)+'*'*(2*a+1))
'''
#99乘法表
#end在格式化输出中表示不换行显示
for i in range(1,10):
    for j in range(1,i+1):
        #print(i,j)
        print(str(i)+'*'+str(j)+'='+str(i*j),end=" ")
    print()
