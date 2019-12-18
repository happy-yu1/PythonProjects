from multiprocessing import Process
import time
import os


# 单进程时
# i=15
# while i>0:
#     print('----1---')
#     i-=1
#
# j=10
# while j>0:
#     print('----2---')
#     j-=1

# 多进程时

def proc1():  # 传入不带参数的函数
    j = 10
    while j > 0:
        print('----2---')
        j -= 1
    time.sleep(2)

def proc2(n):  # 传入带有一个参数的函数
    k = 20
    while k > 0:
        print('----2---%d' % n)
        k -= 1
    time.sleep(2)

def proc3(x, y):  # 传入带有多个参数的函数
    h = 20
    while h > 0:
        print('----2---%d,%d' % (x, y))
        h -= 1
    time.sleep(2)

def proc4(x, **y):  # 传入带有不确定参数的函数
    l = 20
    while l > 0:
        print('----2---%d: %d' % (os.getpid(),x))
        print(y)
        l -= 1
    time.sleep(2)
if __name__ == '__main__':
    p1 = Process(target=proc1)  # 创建子进程——实例化，传入函数
    p2 = Process(target=proc2, args=(123,))
    p3 = Process(target=proc3, args=(123, 234))
    p4 = Process(target=proc4, args=(123,), kwargs={'M': 3})

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    # p4.join()
    # p4.terminate()
