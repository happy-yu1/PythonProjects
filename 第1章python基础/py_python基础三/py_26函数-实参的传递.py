# 不可变数据类型：字符串、数字、元组
def m(a):
    a+=1
    print('函数内取值：%d'% a)
l=10
m(l)  # l为数字型数据，m(l) 和print(l)的输出结果是不一样的
print(l)
print('-'*40)
# 可变数据类型：列表，集合，字典
def n(b):
    b.append('666')
l2=[1,2,3]
n(l2)   # l2为列表，n(l2) 和print(l2)的输出结果是一样的
print(l2)