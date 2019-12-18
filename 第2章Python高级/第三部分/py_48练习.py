def func():
    psw=input('请输入密码：')
    if len(psw)>=8:
        return psw
    # else:
    raise Exception('密码长度<8')

try:
    user=func()
    print(user)
except Exception as e:
    print(e)