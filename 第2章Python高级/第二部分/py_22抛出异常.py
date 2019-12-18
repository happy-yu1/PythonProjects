# raise为主动抛出异常的方法，一般基层次会选择抛出异常，其调用者进行异常处理
def func():
    i = input('请输入：')
    if len(i) < 8:
        raise Exception('长度不够')  # raise 异常类对象 主动抛出异常
    else:
        return i


if __name__ == '__main__':
    r = None
    try:  # 外界进行调用时，有发生异常的可能，则调用的时候进行异常处理
        r = func()
    except Exception:
        print('exception')
    print(r)
    # r=func()
    # print(r)
