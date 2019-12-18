
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点的坐标为(%d,%d)' % (self.x, self.y)


class Circle:
    def __init__(self, r, point):
        self.r = r
        self.o = point

    def __str__(self):
        return '半径为：%d,圆心为：（%d,%d)' % (self.r, self.o.x, self.o.y)

class App:

    def peng(self):
            a = c1.o.x - c2.o.x
            b = c1.o.y - c2.o.y
            if (a ** 2 + b ** 2) ** 0.5 > (c1.r + c2.r):
                print('没有发生碰撞')
            else:
                print('碰撞')

if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(4, 3)
    print(p1)
    print(p2)
    c1 = Circle(3, p1)
    c2 = Circle(4, p2)
    print(c1)
    print(c2)
    print('*' * 40)

    # a = c1.o.x - c2.o.x
    # b = c1.o.y - c2.o.y
    # if (a ** 2 + b ** 2) ** 0.5 > (c1.r + c2.r):
    #     print('没有发生碰撞')
    # else:
    #     print('碰撞')
    a1=App()
    print(a1.peng())
