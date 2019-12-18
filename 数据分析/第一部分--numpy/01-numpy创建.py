import numpy as np
import matplotlib.pyplot as plt
import random
x=range(1,10)
'''
y=[]
for i in x:
    y.append(i)

m=plt.plot(x,y)
# print(m)
'''
#一、创建一维数组，创建一个numpy.ndarray对象，a是一个一维数组
#法一：
a=np.array(x)  #[1 2 3 4 5 6 7 8 9]
# print(type(a),a)
#法二：
b=np.array([2,3,4,5,6,7])
print(type(b),b)
#法三：
c=np.arange(1,10)
print(type(c),c)

d=np.random.random(9)  #随机生成两个小数
print(d)

p=plt.plot(c,d)
plt.show(p)   #将图形显示出来