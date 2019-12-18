def cunm(a, b):
    return a+b
cunm(2, 3)  # 不返回值

a=cunm(2, 3) # 返回接收值
print(a)


def cunm(a, b):
    return a, b  # 返回多个值


x, y = cunm(1, 2)
print(x)
print(y)


f=lambda age,score:age+score
m=f(4,5)
print(m)