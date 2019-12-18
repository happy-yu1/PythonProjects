import numpy as np
import matplotlib.pyplot as plt
import random
#一、绘制出猪肉价格的直方图
# 读取本地的train.csv文件
# Piglet 	LiveHog 	Pork	feed	corn	soybean（大豆），第三列为生猪价格，若要求生猪价格的均值,最大值，最小值
'''
t = np.loadtxt('trainx.csv', delimiter=',', skiprows=1, dtype='float')
# print(t,t.shape)   #(58, 6)
t_pork = t[:, 2]
print(t_pork.mean(), t_pork.max(), t_pork.min())  # ---22.401034482758625  30.35   15.46

# 进行分组，根据极差大小进行划分,但有时候不准，如果最大值10000很大，最小值2很小，而且最大值附近的数并不是很多时，观察数据较为集中在哪个范围，然后将数值较大且个数不多的数据去除掉，再进行分组会更合适一点

# print(type(bin_nums))

d = 3
bin_nums = int(((t_pork.max()) - t_pork.min()) // d)
# 绘图
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(t_pork, bin_nums)
# 展示
# plt.show()
'''
#二、希望了解猪肉价格（第三列）和大豆价格（最后一列）的关系----绘制散点图（不需要分组）
'''
t_bean=t[:,-1]
print(t_bean)
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(t_bean,t_pork)
plt.show()

#根据图形结果，t_bean<3.3的数据和猪肉价格没有什么关系，如果只想要后面关系明显的，尝试如下：
t = np.loadtxt('trainx.csv', delimiter=',', skiprows=1, dtype='float')
t_pork = t[:, 2]
t_bean=t[:,-1]
t_bean=t_bean[t_bean>3.3]
#如此操作会报错，因为只改变了t_bean的数据多少，而t_pork仍是以前的数据，会出现x，y个数不匹配的现象，需要在读取t的时候就要进行相应操作
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(t_bean,t_pork)
plt.show()
'''
#进一步的修改如下：
t = np.loadtxt('trainx.csv', delimiter=',', skiprows=1, dtype='float')
t=t[t[:,-1]>3.3]   #将大豆价格<=3.3的行数据删除掉了，猪肉价格的数据和大豆价格数据保持一致
t_pork = t[:, 2]
t_bean=t[:,-1]
t_bean=t_bean[t_bean>3.3]
#如此操作会报错，因为只改变了t_bean的数据多少，而t_pork仍是以前的数据，会出现x，y个数不匹配的现象，需要在读取t的时候就要进行相应操作
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(t_bean,t_pork)
plt.show()