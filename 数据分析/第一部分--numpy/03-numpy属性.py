import numpy as np
import matplotlib.pyplot as plt
import random
'''

a=np.array([2,3,4,5,6,7])
b=np.array([2.1,3.44,4,5.1,6.1,7.1])
c=np.array([True,False,False,True])

#1、  显示dtype属性
print(a.dtype)    #----int32  [2,3,4,5,6,7]
print(b.dtype)    #----float64
print(c.dtype)    #----bool

#2、  设置dtype属性
a1=np.array([2,3,4,5,6,7],dtype='i1')  #i1表示int8，，i2表示int16……
a2=np.array([2,3,4,5,6,7],dtype='bool')

print(a1.dtype)    #----int8,由之前的----int32变成int8
print(a2.dtype,a2)    #----bool  [ True  True  True  True  True  True]

#3、  修改dtype属性----astype（）函数
a3=a1.astype('int32')
print(a3.dtype)    #----int32,由int8变成int32
'''
#4、其他属性
t=np.arange(12).reshape(3,4)
print(t.ndim)   #ndim属性可以输出当前数组时几维的，2则表明是2维的
print(t.size)   #输出当前数组共有几个数据---12