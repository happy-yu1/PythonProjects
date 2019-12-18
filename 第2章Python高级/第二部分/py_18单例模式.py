class Single:  # Single后无父类名，默认父类为Object类，Object类为所有类的基类
    instance = None  # 定义类属性，
    init_flag = False

    def __new__(cls, *args, **kwargs):  # 该类方法为对象分配存储空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 利用父类分配空间的方法为其进行空间的分配
        return cls.instance

    def __init__(self):
        if not Single.init_flag:   #'''not x 为布尔“非”，若x为false，则返回true；
            # 若x为true，返回false,通过这个判断，不论创建多少个对象，__init__中的内容只会出现一次

            print('love xie_wei')
            Single.init_flag = True


class Nural:
    def __init__(self):
        pass


if __name__ == '__main__':
    s1 = Single()
    s2 = Single()
    print(s1)  # s1  s2 的内存空间相同
    print(s2)
    print('*' * 40)

    n1 = Nural()
    n2 = Nural()
    print(n1)  # n1  n2 的内存空间不同
    print(n2)
