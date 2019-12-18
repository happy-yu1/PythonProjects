class Base:
    num = 10

    def __init__(self):
        self.basename = 'basename'


class Sub(Base):
    num = 11  # 类属性的重写，并不会改变父类类属性的值

    def __init__(self):
        super().__init__()
        self.basename = 'sub_name'  # 实例属性的重写
        self.subname = 'subname'


if __name__ == '__main__':
    print(Base.num)  # 类属性的调用不需要创建对象
    print(Sub.num)

    b = Base()
    s = Sub()

    print(b.basename)  # 实例属性的调用需要创建对象
    print(s.basename)
    print(s.subname)
