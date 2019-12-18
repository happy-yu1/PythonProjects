# 同一进程下的多线程间可以实现数据共享，但多进程间相互独立，数据（包括全局变量）均不可共享

# import threading
from multiprocessing import Process
import time

g_num = 0


def work1(num):
    global g_num  # 将g_num定义为全局变量
    for i in range(num):
        g_num += 1
    print('---in work1,g_num is %d---' % g_num)


def work2(num):
    global g_num  # 将g_num定义为全局变量
    for i in range(num):
        g_num += 1
    print('---in work2,g_num is %d---' % g_num)


if __name__ == '__main__':
    #多线程间子线程对g_num的操作会彼此影响，最终导致g_num为二者之和
    # t1 = threading.Thread(target=work1, args=(1000000,))
    # t2 = threading.Thread(target=work2, args=(1000000,))

    # 子进程间对g_num的操作彼此独立，且不影响主进程，最终导致主进程中g_num任为最初值0
    t1 = Process(target=work1, args=(1000000,))
    t2 =Process(target=work2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(3)  # 将主线程进行暂停，等待以上结果全部执行完成后再进行print(g_num)

    print(g_num)
