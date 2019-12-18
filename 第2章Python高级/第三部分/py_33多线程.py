import threading
# from threading import Thread 不能用这种方法，因为是导入模块，
# 后面会用到模块内的方法，不仅仅使用里面的Thread类
import time


def func():
    i = 20
    while i > 0:
        print('----%s---' % threading.current_thread().name)  # 显示当前线程的名字
        i -= 1
        time.sleep(0.1)


if __name__ == '__main__':
    t = threading.Thread(target=func, name='hello')  # name方法可以定义子线程的名字
    lenth = len(threading.enumerate())  # '''获取当前线程的数量，1个，
    # 说明只有执行start（）方法后，子线程才被启动
    print(lenth)

    t.start()
    lenth = len(threading.enumerate())  # 获取当前线程的数量 ,2个
    print(lenth)

    i = 20
    while i > 0:
        i -= 1
        print('----%s---' % threading.current_thread().name)
        time.sleep(0.1)

    lenth = len(threading.enumerate())  # 获取当前线程的数量，1个
    print(lenth)