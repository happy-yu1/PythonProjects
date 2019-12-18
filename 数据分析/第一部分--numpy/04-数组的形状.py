import numpy as np
import matplotlib.pyplot as plt
import random
a=np.array([2,3,4,5,6,7])
b=np.array([[2,3,4,5,6,7],
           [2, 3, 4, 5, 6, 7]])
b1=np.array([[2,3,4,5,6,7]])
c=np.array([b,b,b])
#1.1 shape属性查看数组形状
print(a.shape)   #(6,)一维数组
print(b.shape)      # (2, 6)  二维数组
print(b1.shape)      #(1, 6)  二维数组 ,只有一行
print(c.shape)      #(3, 2, 6)  三维数组

print('*'*10)
#1.2 数组间维数的转变，总元素不变法则
#如a是一维数组，总共有6个元素，可以转成2*3的二维和1*3*2的三维
a2=a.reshape(2,3)
a3=a.reshape(1,3,2)
print(a2)
print(a3)
print('*'*10)

#当b是一个多维数组，转变成一维数组时，以下答案一样
b2=b.reshape(12,)  #已知b内有12个元素
b3=b.reshape((b.shape[0]*b.shape[1],))  #不知b内有多少个元素时--法一
b4=b.flatten()   #不知b内有多少个元素时--法二，，flatten()展开的意思，按行从前往后展开
print(b2)
print(b3)
print(b4)

# t=np.arange(1,7).reshape(3,2)  # (3, 2)  二维数组
# t1=np.arange(3).reshape(3,1)  # (3, 1)  二维数组
# t2=np.arange(4,7).reshape(1,3)  # (1, 3)  二维数组
# t3=np.arange(3)          # (3, )  一维数组
# t4=np.arange(9).reshape(3,3)
#
# print(t-t1)

