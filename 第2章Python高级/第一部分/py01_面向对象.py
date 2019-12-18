class Cat:    #  定义一个猫类
    def __init__(self,name):
        self.name=name
        print('HHHH')
    def eat(self):
        Cat.a=2
        print('猫吃鱼')

    def drink(self):
        print('猫喝水')
        print(Cat.a)
c=Cat()    # 实例化一个猫类对象
# c.eat()    #  通过猫类对象调用方法
c.drink()
# print(c)   #  at后面的一串数字为变量c的存储空间
