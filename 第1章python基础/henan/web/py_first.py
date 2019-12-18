userinfo={}
def register():
    global userinfo
    name=input('请输入姓名:')
    if name in userinfo:
        print('用户名已被占用')
        return
    else:
        pas=int(input('请输入密码:'))
        print('注册成功')
        userinfo[name]=pas

def logging():
    global  userinfo
    name=input('请输入姓名:')
    pas = int(input('请输入密码:'))
    if name in userinfo and userinfo[name]==pas:
        print('登录成功')
    else:
        print('账户或密码错误')
    # if name in userinfo:
    #     if userinfo[name]==pas:
    #         print('登录成功')
    #         return
    #
    # print('账户或密码错误')

if __name__ == '__main__':
    while True:
        print('注册：1  登录：2   退出：3')
        i = int(input('请选择：'))
        if i==1:
            register()
        elif i==2:
            logging()
        else:
            print('欢迎下次再来')
            break


