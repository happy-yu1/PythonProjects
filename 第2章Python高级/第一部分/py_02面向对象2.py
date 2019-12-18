class Cat:
    def __init__(self, name):  #  此处将属性特殊化，name就是一个特殊的属性/参数
        self.name = name
        pass

    def eat(self):
        print('%s爱吃鱼' % self.name)

    def drink(self):
        print('%s爱喝水' % self.name)

tom=Cat('Tom')   #Tom即为name的一个具体表现
tom.eat()
tiger=Cat('Tiger')
tiger.drink()