class Base:
    def __init__(self, basename):
        self.__basename = basename


class Sub(Base):
    def __init__(self, basename, subname):
        super().__init__(basename)
        self.subname = subname

    def func(self):
        # print(self.__basename)   #私有属性不可以访问，否则会报错
        print(self.subname)


if __name__ == '__main__':
    b = Base('base')
    s = Sub('base','sub')

    s.func()
