t=('name','sex','age')
d1=dict.fromkeys(t)
print(d1)
d2=dict.fromkeys(t,'aaa')  # 对d2中键对应的值进行统一赋值
print(d2)


d = {'name': 'zhang3', 'score': 34, 'age': 10}

# 以下两种方法均可以调出键对应的值，第二个比较常用
print(d['name'])
print(d.get('name'))
print('%s:%s' % ('name',d['name']))   # 同时输出键值对
print('-'*40)

dict = {'sex': 'zhang3', 'score': 34, 'age': 10}
print(dict.items())
for (k,v) in dict.items():  # 遍历dict中的每队键值对，并简单明了的输出（法一）
    print('%s:%s' % (k,v))

for k in dict.keys():  # 输出所有的键（法一）
    print(k)
print('-'*40)
for v in dict.values():   # 输出所有键对应的值
    print(v)

for k in dict.keys():  # 输出所有的键值对（法二）,不常用
    print('%s:%s'% (k,dict[k]))
for k in dict:  # 输出所有的键 （法二），因为键是唯一的，可以这样用，但是值不是唯一的，不可以这么用，必须加上.values()
    print(k)