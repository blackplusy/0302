#coding=utf-8
#实参位置
def animal(pet1,pet2):
    print(pet1+' wang!'+pet2+' miao!')

animal('2ha','bosi')
animal('jiafei','taitan')

#关键字参数
def animal(pet1,pet2):
    print(pet1+' wang!'+pet2+' miao!')

animal(pet2='cat',pet1='fadou')

#参数默认值
def animal(pet2,pet1='2ha'):
    print(pet1+' wang!'+pet2+' miao!')

animal('bosi')
animal('jiafei','keji')
#不定长
def test(x,y,*args):
    print(x,y,args)

test(1,2,'heygor','ladeng')

def test1(x,y,**args):
    print(x,y,args)

test1(1,2,a=10,b='gaga')

