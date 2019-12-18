import threading
import time
# import os


class MyThread(threading.Thread):
    def __init__(self, begin, end):
        super().__init__()
        self.begin = begin
        self.end = end

    def func(self,n):
        for x in range(2, n):
            if n % x == 0:
                return False
            else:
                return True

    def run(self):
        for i in range(self.begin,self.end):
            if self.func(i):
                print('%s:%d是素数' % (threading.current_thread().name, i))
            # time.sleep(0.1)


if __name__ == '__main__':
    t1 = MyThread(3, 1001)
    t2 = MyThread(1001, 2001)
    t3 = MyThread(2001, 3001)

    t1.start()
    t2.start()
    t3.start()
