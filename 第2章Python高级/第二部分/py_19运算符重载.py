class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # __add__ 方法的重写，向量加向量仍为向量
        return Vector(self.x + other.x, self.y + other.y)
        # print( Vector(self.x + other.x, self.y + other.y))

    def __str__(self):
        return 'vector(%d.%d)' % (self.x, self.y)


if __name__ == '__main__':
    v1 = Vector(10, 13)
    v2 = Vector(8, 15)
    print(v1 + v2)  # 用这种方法就可以，如果没有重写__add__ 方法，则会报错
    # v1.__add__(v2)
    print('*' * 40)
    a = 10
    b = 20
    print(a + b)
