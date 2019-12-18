class Tool:
    a = 0

    @classmethod
    def clsfunc(cls):
        print('类方法')

    def __init__(self, name):
        self.name = name
        Tool.a += 1  # 类属性的调用：类名.类属性

    def func2(self):
        print('实例方法')

    print('%d' % a)


if __name__ == '__main__':
    t1 = Tool('锤子')  # 每增加一个实例对象，__init__()方法就会执行一次，a的值就会增加1
    t2 = Tool('剪刀')

    Tool.clsfunc()  # 不用创建对象便可调用类方法，通过类名.类方法（） 进行调用
    t1.func2()  # 实例方法需要创建对象，通过对象.实例方法（） 进行调用
    print(Tool.a)
