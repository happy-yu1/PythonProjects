from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
import numpy as np

# y为十点到12点每分钟的气温(20,35)，作出气温、时间变化图
'''
x=range(120)  #--range类型,不可以取步长，需转换成列表形式才可以取步长
print(type(x),x)
y=range(2,10,2)
print(type(y),y)
z=[i for i in range(20)]   #列表，可以取步长

y=random.randint(2,6)  #只能取出一个随机数
print(y)
y2=np.random.randint(20,35,120)
print(type(y2),y2)
'''
# 第一步，简单作图
x = range(120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)  # figsize尺寸，dpi像素大小

fig = plt.plot(x, y)

# 保存图片
plt.savefig('tempreture.png')
# plt.show()

# 修改x轴的刻度，通过取步长的方法

# 1、将x轴的0~120数值型的120个数据转变成字符串形式：10点0分，10点20分，11点0分……，也包含120个
xtick_labels = ['10点{}分'.format(i) for i in range(60)]
xtick_labels += ['11点{}分'.format(i) for i in range(60)]

plt.xticks(list(x),xtick_labels)  #将x轴的刻度变成字符串形式的
 #以3为步长,数值型和字符串格式的要同步，可将字符串进行45度倾斜，rotation逆时针
plt.xticks(list(x)[::3],xtick_labels[::3],rotation=45)
plt.plot(x,y)
# plt.show()

#将未显示出来的中文显示出来
my_font=font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
plt.xticks(list(x)[::3],xtick_labels[::3],rotation=45,fontProperties=my_font)
plt.plot(x,y)
# plt.show()

#添加x、y轴和标题信息
plt.xlabel('时间',)
plt.ylabel('气温 单位（摄氏度）')
plt.title('10点到12点每分钟气温变化情况')

#添加网格
plt.grid()
#设置透明度,1表示完全不透明
plt.grid(alpha=0.4)