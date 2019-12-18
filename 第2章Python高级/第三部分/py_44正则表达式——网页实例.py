from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

d = {'a': '2', 'b': '3' }
for x, y in d.items():
    print(x, y)

l=[k + '=' + v for k,v in d.items()]
print(l)


l1=[x*x for x in range(1,11) if x%2 ==0]
print(l1)  # 显示生成后的内容
print(type(l1))   #列表

g1 = (a * a for a in range(5))
print(g1)   # 出现存储空间，而不是显示生成后的内容
print(type(g1))   #生成器

print(next(g1))






# def func(a) -> int:
#     a = 10
#     print(a)
#     return 0
#
#
# func(20)
# print('---1---')
# print(func(20))
#
# for i in 'asdf':
#     print(i,end=' ')
