# 自定义异常类，就是重写异常类父类的__init__()方法


class Myexception(Exception):
    def __init__(self, error):
        self.error = error  # error表示错误信息


def func():
    i = input('请输入：')
    if len(i) < 8:
        raise Myexception('长度小于8')
    else:
        return i


if __name__ == '__main__':
    r = None
    try:
        r = func()
    except Myexception as e:
        print(e)  # 输出的内容可以自定义，也可以用抛出异常时显示的信息：长度小于8
        # print('myexception')  自定义要输出的内容

    print(r)
