# 多线程同步的时候，当变量特别大时，会发生资源竞争，
# 导致结果出现混乱，为解决这一问题，引入互斥锁的思想：Lock（）类

import threading
import time

g_num = 0




def work1(num):
    global g_num  # 将g_num定义为全局变量
    for i in range(num):
        mutex.acquire()  # 锁定
        g_num += 1
        mutex.release()  # 解锁
    print('---in work1,g_num is %d---' % g_num)


def work2(num):
    global g_num  # 将g_num定义为全局变量
    for i in range(num):
        mutex.acquire()
        g_num += 1  # 会导致资源竞争的代码
        mutex.release()
    print('---in work2,g_num is %d---' % g_num)


if __name__ == '__main__':
    mutex = threading.Lock()  # 创建锁

    t1 = threading.Thread(target=work1, args=(1000000,))

    t2 = threading.Thread(target=work2, args=(1000000,))
    t1.start()
    t2.start()
    while len(threading.enumerate()) != 1:  # 当现在运行的子线程数不为1 时，暂停1秒钟
        time.sleep(1)
    print(g_num)
