# 关键字参数
def h(name, age):
    print('姓名是：%s' % name)



# a = 'zhang3'
# b = 50


# 不定长度参数-以元组形式存储参数
def m1(a, *b):
    print(a,end=' ')
    print(b)


m1(1)
m1(1, 2, 3)
print('-' * 40)


def m2(a, *b):
    print(a,end=' ')
    for i in b:
        print(i,end=' ')


m2(1)
m2(1, 2, 3)
print(' ')
print('-' * 40)

# 不定长度参数-以字典形式存储参数
def m3(a, **b):
    print(a,end=' ')
    print(b)


m3(1)
m3(1, x=2, y=3)
print('-' * 40)


def m4(a, **b):
    print(a,end=' ')
    for k,v in b.items():
        print('%s:%d'% (k,v),end=' ')


m4(1)
m4(1, x=2, y=3)
print(' ')
print('-' * 40)
# 命名关键字参数
def m5(a,*,b,c):
    print(a)
    print(b)
    print(c)
# m5(1)
# m5(1,b=2)
m5(1, b=2,c=3)
# m5(1,b=2,c=3,d=4)