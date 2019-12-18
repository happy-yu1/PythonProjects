# 调用被封装的属性和方法，采用get 和set 函数

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def eat(self):
        print('%s在吃饭' % self.__name)

    def func1(self):  # 该方法以便显示被封装的属性
        return self.__name

    def func2(self, name):  # 该方法以便更改被封装后属性值
        self.__name = name


if __name__ == '__main__':
    p1 = Person('zhang3', 16)
    print(p1.func1())  # 可以显示出被封装的属性

    p1.eat()
    print('*' * 40)
    p1.func2('li4')  # li4的更改有效
    p1.eat()
