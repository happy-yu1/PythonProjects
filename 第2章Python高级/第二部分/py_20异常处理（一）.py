# 异常处理针对的是预知的到但是没法控制的情况


class Base:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def func(self):
        r = None
        try:  # 异常处理用 try…… except……
            r = (self.x / self.y)  # 会出现异常的代码
        except ZeroDivisionError:  # ZeroDivisionError 为Excepttion类的子类，表示除数为0
            print('除数为0')
            exit()  # 若想发生错误后便结束程序，可用exit()，后面的便不会再执行
        except TypeError:  # 类型错误
            print('除数为字母')
        finally:  # 无论是否发生异常，都会执行的代码
            print(r)
        # return r


class Sub(Base):

    def __init__(self, x, y):
        super().__init__(x, y)


if __name__ == '__main__':
    s1 = Sub(4, 2)
    s1.func()

    print('*' * 40)

    s2 = Sub(4, 0)
    s2.func()

    print('*' * 40)

    s3 = Sub(4, 'a')
    s3.func()
