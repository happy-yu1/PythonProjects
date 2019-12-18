class Auto:
    def __init__(self, brand):
        self.brand = brand

    def charge(self, days):
        pass


class Car(Auto):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def charge(self, days):    #计价
        if self.brand == '别克':
            if self.model == 'x':
                money = days * 500
        elif self.brand == '宝马':
            if self.model == 'y':
                money = days * 800
        return money

class Service:   #服务员提供收费金额
    def pay(self,auto,days):   #该方法体现了多态的思想，含有charge（）方法的均可以被service实例化的对象调用
        print(auto.charge(days))


if __name__ == '__main__':
    s=Service()
    c=Car('别克','x')
    s.pay(c,5)
