class HouseItem:  # 定义家具类
    def __init__(self, name, area):  # 添加两个属性即变量：名称、占地面积
        self.name = name  # self.name和self.area为形参，可接收外部的参数
        self.area = area

    def __str__(self):
        return '%s占地:%.2f' % (self.name, self.area)


class House:
    def __init__(self, type, area):  # type（房型）和area（房屋面积）需要从外界传入，所以设置这两个属性
        self.type = type
        self.area = area
        self.free_area = area
        self.item_list = []

    def add_item(self, item):  # '''此处的item仅表示需要从外界传递参数,
        # 但具体传递的对象是什么由实际操作决定:可以是一般的数据类型，也可以是其他类中已经定义的对象'''
        if self.free_area - item.area >= 0:
            self.free_area -= item.area  # 此处传递的item即为HouseItem中定义的一个对象
            self.item_list.append(item.name)
        else:
            print('空间不足')

    def __str__(self):
        return '''户型:%s,占地面积：%.2f[剩余面积：%.2f]，家具:%s''' \
               % (self.type, self.area, self.free_area, self.item_list)


if __name__ == '__main__':
    A = HouseItem('bed', 4)  # 家具例化后的一个对象
    B = HouseItem('table', 6)
    h1 = House('两户', 15)  # 房子例化后的一个对象
    h2 = House('三户', 20)
    print('*' * 40)
    print(A)
    print(h1)
    print('*' * 40)
    h1.add_item(A)  # 为房子h1添加家具：bed
    print(h1)
    print('*' * 40)
    h1.add_item(B)  # 再为房子h1添加家具：table
    print(h1)
    print('*' * 40)
    h1.add_item(B)  # 再为房子h1添加家具：table
    print(h1)  # 此时显示空间不足
