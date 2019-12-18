a = None


def func():
    if not a:
        return True
    else:
        return False


def input_passward():
    psw=input('请输入密码：')
    if len(psw)>=8:
        return psw
    else:
        ex=Exception('密码长度<8')
        raise ex



if __name__ == '__main__':
    # print(func())
    # try:
    #     user_psw = input_passward()
    #     print(user_psw)
    # except Exception:
    #     print('错误')
    # except Exception as e:
    #     print(e)
    # # input_passward()
    g1=(4,6,9,10)




