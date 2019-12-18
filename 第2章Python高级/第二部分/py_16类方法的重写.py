class Base:

    def __init__(self):
        self.basename = 'basename'

    @classmethod
    def clsfunc(cls):
        print('父类clsfunc()')

    def base_func(self):
        print('basename')


class Sub(Base):

    def __init__(self):
        super().__init__()
        self.subname = 'subname'

    @classmethod
    def clsfunc(cls):  # 类方法的重写
        print('重写clsfunc()')

    def base_func(self):  # 实例方法的重写
        print('sub_name')
        super().clsfunc()  # 无论是否重写，类内调用父类的类方法（，此处是调用被重写的父类，类方法）
        Base.clsfunc()  # 调用自己的类方法
    def sub_func(self):
        print('subname')

    def func(self):
        # a.sub_func()  #调用自己的实例方法,其中a为一个实例对象
        # sub_func()
        pass
if __name__ == '__main__':
    Base.clsfunc()  # 无论类方法是否被重写，类外调用方式一样：类名.类方法（）,
    Sub.clsfunc()
    print('*' * 40)

    b = Base()
    s1 = Sub()
    super(Sub,s1).clsfunc()
    # 父类方法被重写后，子类仍想调用父类类方法的办法：super（子类名，子类对象）.被重写的父类方法名（）
    s2= Sub()
    b.base_func()
    s1.base_func()
    s1.sub_func()
    print('*' * 40)

    super(Sub,s1).base_func()  # 实例方法被重写后，类外调用方法
    super(Sub,s1).clsfunc()
    print('*' * 40)

    # s2.func(s1)  # s1为一个对象
