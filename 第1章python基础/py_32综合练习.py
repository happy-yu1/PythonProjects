userinfo={}
def register():
    global userinfo
    name=input('请输入用户名：')
    if name in userinfo:
        print('用户名已存在')
    else:
        passwd=int(input('请输入密码：'))
        userinfo[name]=passwd
        print('注册成功')

def login():
    global userinfo
    name = input('请输入用户名：')
    passwd=int(input('请输入密码：'))
    if name in userinfo:
        if passwd==userinfo[name]:
            print('登录成功')
            return
    print('用户名或者密码错误')



def main():
    pass
while True:
    print('*'*20)
    print('1、注册')
    print('2、登录')
    print('3、退出')
    print('*' * 20)
    i=int(input('请输入：'))

    if i==1:
        register()
    elif i==2:
        login()
    elif i==3:
        print('欢迎再次使用本系统')
    else:
        print('输入有误')

if __name__ == '__main__':
    main()