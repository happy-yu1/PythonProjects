class Base:
    a = 0  # 初始化 类属性

    @classmethod  # 类方法 的修饰器
    def func1(cls):
        print('类方法')

    @staticmethod  # 静态方法，不可调用有任何其它类属性、方法，实例属性、方法
    def func2():
        print('静态方法')
    def __init__(self):  # 实例属性
        self.name = 'base'

    def func3(self):
        print('实例方法')

if __name__ == '__main__':
    b=Base()
    b.func1()
    b.func2()
    b.func3()