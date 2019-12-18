import re
# from collections.abc import Iterable
# print(isinstance((1,2,3),Iterable))
# l=(1,'abc',2,3)
# d={'a':'1','b':'2'}
# print([k+'='+v for k,v in d.items()])
# i=iter(l)
# print(i)
# for x in i:
#     print(x,end=' ')
# print('\n')
# m=(k+'='+v for k,v in d.items())
# # print(m)
# for i in m:
#     print(i)
# print(next(i))

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# s4 =r'([a-z][0-9]{3})--([0-9][a-z]{3})--\2--\1$'
# print(re.match(s4,'s123--1asd--1asd--s123').group())
# s =r'(?P<g1>[a-z][0-9]{3})--(?P<g2>[0-9][a-z]{3})--(?P=g2)--(?P=g1)'
# print(re.match(s,'s123--1asd--1asd--s123').group(1))

# def func(i):
#     stri=i.group()
#     inti=int(stri)
#     inti+=1
#     return str(inti)
# l='a:1 b:3 c:4'
# s=' |:'
# list=re.split(s,l)
# print([list[i] for i in range(len(list)) if i %2 !=0])
# c=lambda x,y:x*y
# print(c(2,3))
# ret=re.compile('[0-9]{3}')
# print(ret.search('h223h456').start())



def odd(x):
    n, a, b = 0, 0, 1
    while n < x:
        yield (b)
        a, b = b, a + b
        n += 1
        return 'done'
o=odd(5)
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
