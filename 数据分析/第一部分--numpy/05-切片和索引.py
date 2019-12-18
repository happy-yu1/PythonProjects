import numpy as np

t=np.arange(12).reshape(3,4)  # (3, 4)  二维数组
# print(t)
'''
t1=t[:,1]  #取第二列---法一
t2=t[:,1:3]

print(t2)
np.clip(22,33)
np.clip(a_min=3,a_max=5)
t3=np.clip(t,a_min=3,a_max=5)
t3=np.clip(t,3,5)
print(t3)
print(t)

'''
'''
print(t.shape[1])   #4  表示4列
print(t.shape[0])   #3  表示3行
print(t.dtype)   #  int32


t=t.astype(float)
# print(t.dtype)   #  float64
t[2,2:]='nan'  #将某个数据修改为nan类型
print(t)
for i in range(t.shape[1]):
    line=t[:,i]  #选取第i列，并组成line数组
    nan_num=np.count_nonzero(line!=line)  #计算该列中nan的个数
    if nan_num!=0:   #表明存在nan元素
        not_nan_line=line[line==line] #将第i列中非nan元素提取出来，重新组成一个数组
        not_nan_line.mean()  #计算非nan数组的均值
        line[np.isnan(line)]= not_nan_line.mean()
    #line[np.isnan(line)]的作用是将line中nan元素选中，以便将其修改为line列中其他非nan元素的均值
# print(t)
t3=t.clip(3,5)
print(t3)
'''
