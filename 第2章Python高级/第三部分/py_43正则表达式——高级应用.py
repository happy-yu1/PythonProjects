import re

t1 = re.search('[a-z]+', '1a22b').group()
print(t1)
print(type(t1))  # 字符串
print('---1---')

t2 = re.findall('[0-9]+', '1a22b')
print(t2)
print(type(t2))  # 列表
print(t2[0])
print(type(t2[0]))  # 字符串
print('---2---')

t3 = re.sub('[0-9]+', '33', '1a22b')
print(t3)
print(type(t3))  # 字符串
print('---3---')


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub('[0-9]+', add, '1a22b')
print(ret)

str = 'a:123 b:123 c:123'
reg = ':| '
ret = re.split(reg, str)
print(ret)  # 列表
print([ret[i] for i in range(len(ret)) if i % 2 != 0])

print('---4----')
m = re.compile('[0-9]{2}')
n1 = m.match('22as')
n2 = m.search('a22s33d44')
n3 = m.findall('a22s33d44')
print(n1)
print(n1.group())
print(n2)
print(n3)
print(n2.end())
print(n2.start())

p = (2, 'a', 'b', 4)
print(p[1:3])

