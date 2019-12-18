class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def eat(self):
        print('%s在吃饭' % self.__name)

    def __drink(self):
        print('%d岁的人在喝水' % self.age)


if __name__ == '__main__':
    p1 = Person('zhang3', 16)
    # print(p1.self.__name)  # __.name为隐藏信息，不会显示出来，该操作无效会报错
    print(p1.age)

    p1.eat()
    p1.__name = 'li4'  # 封装属性：对于隐藏信息，更改无效，仍为zhang3
    p1.eat()
    print('*' * 40)

    # p1.__drink()  # 封装方法：隐藏的方法，无法正常调用，会报错
