d = {'name': 'zhang3', 'score': 34, 'age': 10}
print(type(d))
print(d)
print('-' * 40)
d1 = {'name': 'zhang3', 'name': 'zhang3', 'age': 10}  # 若有重复的，后面的会覆盖前面的元素
print(type(d1))
print(d1)
print('-' * 40)
print(d['name'])  # 使用字典，通过键而不是索引值
print(d['score'])
print(d['age'])
print('-' * 40)
d1['name'] = 'li4'  # 修改值
print(d1)
d1['sex'] = '男'  # 当键不存在时，会新增一个键值对
print(d1)