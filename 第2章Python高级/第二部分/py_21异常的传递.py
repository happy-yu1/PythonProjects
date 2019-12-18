def func1(x):
    # try:
    a = 12 / x
    # except ZeroDivisionError:
    print('func1')


def func2(x):  # '''在不同层次上进行异常处理，得到的结果不同，一般会在调用者层次进行异常处理，
    # 高调用层次，如在func2() 中进行异常处理，func1（）中的内容不会显示，
    # func3中进行异常处理，func2和func1中的内容不会显示。

    try:
        func1(x)
    except ZeroDivisionError:
        print('func2')


def func3(x):
    func2(x)
    print('func3')


def func4(x):
    try:
        a = 12 / x
    except:
        raise  # 因为x值需要外界传入，此时将异常抛出，不进行处理，调用者进行异常抛出即可
    print(a)


if __name__ == '__main__':
    # func3(0)
    try:
        func4(0)
    except ZeroDivisionError:
        print('异常处理')
