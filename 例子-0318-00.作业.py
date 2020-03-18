#coding=utf-8
#dic={'username':'admin','password':'123'}
dic={'admin':'123','heygor':'456'}
while 1:
    username=input('请输入您的用户名: ')
    if len(username)==0 or username not in dic.keys():
        print('您的输入有误请重新输入')
    else:
        print('用户名正确')
        while 1:
            password=input('请输入用户名对应的密码')
            if dic[username]==password:
                print('密码正确')
                break
            else:
                print('密码错误，请重新输入')
        break
