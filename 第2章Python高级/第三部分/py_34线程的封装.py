import threading
import time


class MyThread(threading.Thread):  # 创建一个自己的线程类(子类）
    def run(self):  #重写父类的run（）方法，作为实现线程功能的方法
        i = 20
        while i > 0:
            print('----%s---' % threading.current_thread().name)  # 显示当前线程的名字
            i -= 1
            time.sleep(0.1)


if __name__ == '__main__':
    t1 = MyThread()  # 创建一个子线程
    t1.start()
    t2 = MyThread()  # 创建一个子线程
    t2.start()


