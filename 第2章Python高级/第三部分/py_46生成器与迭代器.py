# g1 = (a * a for a in range(1, 5))  # 创建生成器法一
#
# print(next(g1))  # 用next（）方法获得生成器的值
# print(next(g1))
# print(next(g1))
# print(next(g1))
#
# # print(next(g1))  #会报错，因为超过4次，所以的元素都显示完
# print('-----1-----')
#
# g2 = (a * a for a in range(1, 5))
# for i in g2:  # 用for循环可以防止获取值得过程中出现报错
#     print(i)
# print('-----2-----')
#
#
# def func():
#     yield (1)  # yield()创建生成器法二
#     yield (5)
#     yield (6)
#
#
# f = func()
# print(type(f))  # 类型为生成器
# print(next(f))
# print(next(f))
# print(next(f))
#
# print('-----3-----')


# def func1(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n += 1
#     else:
#         return 'done'

# func1(5)


print('-----4----')

def func2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n += 1


    return 'done'


f2=func2(5)
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))

