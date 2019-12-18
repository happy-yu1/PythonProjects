from multiprocessing import Process
import time
import os

def func1(n):  # 判断某个数是否为素数
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True

def func2():
    for n in range(3, 1001):
        if func1(n):
            print('%d:%d是素数' % (os.getpid(),n)) #得到进城编码
            time.sleep(0.5)

def func3():
    for n in range(1001, 2001):
        if func1(n):
            print('%d:%d是素数' % (os.getpid(),n)) #得到进城编码
            time.sleep(0.5)

def func4():
    for n in range(2001, 3001):
        if func1(n):
            print('%d:%d是素数' % (os.getpid(),n)) #得到进城编码
            time.sleep(0.5)

if __name__ == '__main__':
    p1=Process(target=func2)
    p2 = Process(target=func3)
    p3 = Process(target=func4)

    p1.start()
    p2.start()
    p3.start()
