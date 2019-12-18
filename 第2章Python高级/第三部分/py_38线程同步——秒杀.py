import threading
import time

# from threading import  Thread

# 法一——封装的思想

class User(threading.Thread):
    count = 10  # 定义一个类属性（全局变量）

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while User.count > 0:
            mutex.acquire()
            print('%s成功抢到%d号商品' % (self.name, User.count))
            User.count -= 1
            mutex.release()
            time.sleep(0.1)
        else:
            print('很遗憾，没有了')


# 法二————多参数思想
# count = 10
#
#
# def user(name):
#     global count
#     while count > 0:
#         mutex.acquire()
#         print('%s成功抢到%d号商品' % (name, count))
#         count -= 1
#         mutex.release()
#         time.sleep(0.1)
#     else:
#         print('很遗憾，没有了')


if __name__ == '__main__':
    mutex = threading.Lock()
    # u1 = threading.Thread(target=user, args=('zhang3',))
    # u2 = threading.Thread(target=user, args=('li4',))
    # u3 = threading.Thread(target=user, args=('wang5',))
    u1 =User('zhang3')
    u2 = User('li4')
    u3 = User('wang5')


    u1.start()
    u2.start()
    u3.start()
