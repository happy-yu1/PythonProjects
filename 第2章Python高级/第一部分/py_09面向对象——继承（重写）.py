class Base:
    def __init__(self, base_age):
        self.basename = 'basename'  # 不需要从外界输入的属性
        self.base_age = base_age  # 需要从外界输入的属性

    def base_func(self):
        print('base_func()')


class Sub(Base):

    def __init__(self, base_age, sub_name):
        super().__init__(base_age)  # 继承父类中的属性，因base_age是需要从外界输入的属性，则要标明出来
        self.sub_name = sub_name

    def sub_func(self):
        super().base_func()  # 类内调用父类方法（无论是否重写，都是该发）
        print('sub_func()')
        self.base_func()  # 调用子类

    def base_func(self):  # 父类方法的重写,没有这项时，上方的self.base_func()调用的是父类的，
        # 若有则调用该重写后的方法
        print('sub_func(b)')


if __name__ == '__main__':
    b = Base(20)
    s = Sub(10, 'zhang3')

    s.sub_func()
    super(Sub, s).base_func()   #重写后，类外调用父类的方法
