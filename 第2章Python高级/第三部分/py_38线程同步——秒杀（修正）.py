# 使用之前的方法，因为上锁位置的问题会出现抢到0号或者-1号商品的情况，以下方法进行修正

import threading
import time


class User(threading.Thread):
    count = 10  # 定义一个类属性（全局变量）

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            mutex.acquire()  # 在进行判断之前上锁
            if User.count > 0:
                print('%s成功抢到%d号商品' % (self.name, User.count))
                User.count -= 1
                mutex.release()  # 解锁
                time.sleep(0.1)
            else:
                print('很遗憾，没有了')
                mutex.release()  # 解锁
                break  # 退出循环


if __name__ == '__main__':
    mutex = threading.Lock()

    u1 = User('zhang3')
    u2 = User('li4')
    u3 = User('wang5')

    u1.start()
    u2.start()
    u3.start()
