# 使用多进程输出0~3000之间的素数
# 先用单进程

def func1(n):  # 判断某个数是否为素数
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


def func2():  # 输出范围内的所有素数
    for n in range(3, 3001):
        if func1(n):
            print('%d是素数' % n)


if __name__ == '__main__':
    func2()