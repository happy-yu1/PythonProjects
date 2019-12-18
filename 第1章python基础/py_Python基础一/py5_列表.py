# list1 = [1, 2, 3]
# list2 = [1, 'abc', 3]
# list3 = [1, [2, 5], 3, True]
#
# list4=list3.copy()
#
#
#
# print(list1)
# print(list2)
# print(list3)
# print(list2[1])
#
# print(type(0.2))  # type显示该数据的类型
# print(type(123))
print(type(True))
# print(type('abc'))
#
num = ['a', 'b', 'c']
print(num)
num[1] = 'ABC'
print(num)

num.append('opk')  # 在末尾加入
print(num)
num.insert(1, 'abnm')  # 在中间某个位置加入
print(num)
# num.pop(1)
print(num.pop(1))
del (num[1])
del num[1]
# print(num)
#
l = [1, 1, 2, 3, 4, 5, 6]
l.remove(1)
print(l)
print(min(l))
# print('...........')
# l.remove(1)
# print(l)
#
# m = list('qwerty')
# print(m)
# print(type(m))
#
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'd', 'f']
# l2 = l1[:]
# print(l1)
# print(l2)
# print('-' * 40)
# l1.append(3)
# print(l1)
# l1.insert(1,6)
# print(l1)
print(l1.reverse())
l1.sort()
# print(l2)
#
# print('*'*40)
#
# l3 = [11, 22, 33, 44, 55]
# l4 = l3.copy()
# print(l3)
# print(l4)
# print('-' * 40)
# l3.append(66)
# print(l3)
# print(l4)
#
# print('-'*40)
# list5 = [1, [2, 5], 3, True]
# list6=list5.copy()  # 因为list5中存在可变类型——列表，所以用copy得到的是浅拷贝
# print(list5)
# print(list6)
# print('-'*40)
# list5[1][1]=10
# print(list5)
# print(list6)
