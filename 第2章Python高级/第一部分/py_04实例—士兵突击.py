class Gun:
    def __init__(self, model, bullet_count):  # 抢有型号和子弹容量两个属性,有添加子弹和射击的动作
        self.model = model
        self.bullet_count = bullet_count  # 假设刚开始时枪是填满子弹的

    def shoot(self):
        if self.bullet_count > 0:
            print('哒哒哒……')
            self.bullet_count -= 1  # 开一枪，子弹少一发
        else:
            print('没有子弹了')

    def add_bullet(self, count):  # 为抢添加子弹
        self.bullet_count = count

    def __str__(self):
        return '枪型:%s，子弹容量：%d' % (self.model, self.bullet_count)


class Solider:
    def __init__(self, name, gun):  # 士兵类包含两个属性：姓名和所拿的枪，有开火的动作
        self.name = name
        self.gun = gun  # 调用Gun类中的对象

    def fire(self):
        self.gun.shoot()  # 调用Gun类中的shoot（）方法

    def __str__(self):
        return '%s拿的枪是：%s' % (self.name, self.gun)


if __name__ == '__main__':
    a = Gun('AWM', 3)
    s = Solider('谢伟', a)
    print(a)
    print(s)
    print('*' * 40)
    s.fire()  # 谢伟开火
    s.fire()
    s.fire()
    s.fire()
    a.add_bullet(2)  # 给枪加子弹
    s.fire()
