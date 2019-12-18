import numpy as np
import matplotlib.pyplot as plt
import random
a=np.array([2,3,4,5,6,7])

#1.1、普通数学运算
a1=a**2  #a1仍是一个数组,每个元素为a的平方， [ 1  4  9 16 25 36 49 64 81]
n=np.sqrt(a)  #表示的开方
# print(a,a1,n)

print(np.median(a))  # 计算均值
print(a.std())    # 计算均值
print(np.ptp(a))  # 计算极差--即最大值和最小值之间的差：7-2=5


#1.2  sort（）函数的使用
d=np.random.randint(1,100,10)  #表示在1`100之间生成10个随机的整数
# print(d)  #[15 20 19 30 63 52 93 20 20 20]

#法一：此时改变了d的值，并没有新创建一个数组
d1=d.sort()
# print(d1)  #-----None 没有值
# print(d)    #[15 19 20 20 20 20 30 52 63 93]

#法二：新创建一个数组，并不改变d的值
# d2=np.sort(d)
# print('*'*10,d2)

#1.3 round()函数
t=np.random.random(3)  #在0~1之间生成3个随机小数  [0.87683054 0.29784175 0.98638834]
# print(t)
# t1=np.array([random.random() for i in range(3)])
# print(t1)
m=np.round(t,2) # 将t的结果保留2位小数  [0.88 0.3  0.99]
# print(m)

#1.4 因为a仍是一个数组，可以在a上进一步操作
# b1=np.array([a,a*2])
# # print(type(b1),b1)
# b2=b1.sum(axis=0)
# print(type(b2),b2)
s1=np.arange(12).reshape(3,4)
print(np.hsplit(s1,2))