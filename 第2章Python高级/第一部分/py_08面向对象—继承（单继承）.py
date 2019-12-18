class Base:
    def __init__(self):
        self.basename = 'basename'  # 父类属性不需要从外界传入

    def base_func(self):
        print('base_func()')


class Sub(Base):

    def __init__(self):  # ctrl+o 调用父类属性的快捷键
        super().__init__()  # 继承父类的属性，若父类有从外界传入的属性如：name，则此处应该为__init__(name)
        self.subname = 'subname'  # 子类特有的属性

    def sub_func(self):
        super().base_func()  # 类内调用父类方法
        print('sub_func()')


if __name__ == '__main__':
    b = Base()
    s = Sub()

    print(b.basename)
    b.base_func()
    print('*' * 40)

    print(s.subname)
    print(s.basename)  # 调用父类的属性
    print('*' * 40)

    s.sub_func()
    s.base_func()  # 类外调用父类的方法（父类方法没有被重写时）
