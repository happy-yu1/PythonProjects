import numpy as np
'''

#1、二维数组的读取：loadtxt和savetxt
a=np.arange(50).reshape(5,10)
print(a.shape)  #---(5,10)
np.savetxt('a.csv',a,fmt='%d',delimiter=',')

b=np.loadtxt('a.csv',dtype=int,delimiter=',')
print(b.shape)  #---(5,10)

#2、三维数组的读取：tofile和fromfile
#该方法只能将读取的信息保存为一维，读取时需要重新reshape（）
c=np.arange(100).reshape(5,10,2)
c.tofile('c.csv',sep=',',format='%d')   #变成一维数组了

d=np.fromfile('c.csv',dtype=int,sep=',')
print(d.shape)     #  ---(100,),读取时仍为一维

t=d.reshape(5,10,2)   #---(5, 10, 2)
print(t.shape)

#3、random子库的使用
#生成一个(2,2,2)三维数组，每个元素为[0,1)之间的浮点数，且满足均匀分布
t1=np.random.rand(2,2,2)
print(t1)
print('--1-'*20)

#生成一个(2,2,2)三维数组，每个元素为满足标准正太分布
t2=np.random.randn(2,2,2)
print(t2)
print('--2-'*20)


np.random.seed(10)
t2=np.random.randn(2,2,2)
print(t2)
print('--3-'*20)

t3=np.random.randint(1,100,(3,4))
print(t3)
'''
a=np.arange(50).reshape(5,10)
np.savetxt('a.txt',a,fmt='%d',delimiter=',')

b=np.genfromtxt('a.txt',dtype=int,delimiter=',')
# print(b.shape)  #---(5,10)
# print(b)
# print(help(np.genfromtxt))
c=np.linspace(0,6,10)  #在0~6之间平均取10个值
c1=np.random.randint(0,6,10)
print(c)
