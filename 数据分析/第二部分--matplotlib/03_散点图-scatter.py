#通过爬虫获得北京3月份和10月份每天的最低温度，画出温度随时间变化的散点图

from  matplotlib import pyplot as plt
import  random
from matplotlib import font_manager
x=range(1,32)
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

#做出简单草图
plt.figure(figsize=(20,8),dpi=90)
plt.scatter(x,y_3)
plt.scatter(x,y_10)
# plt.show()

# 修改x刻度范围，使y1和y2的结果分割开
x_3=range(1,32)
x_10=range(51,82)
plt.figure(figsize=(20,8),dpi=90)
plt.scatter(x_3,y_3)  #注意区别
plt.scatter(x_10,y_10)


#添加x轴刻度
x=list(x_3)+list(x_10)
xtick_label=['3月{}日'.format(i) for i in range(1,32)]
xtick_label+=['10月{}日'.format(i) for i in range(1,32)]
my_font=font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  #添加中文字体
plt.xticks(x,xtick_label,fontproperties=my_font,rotation=45)


#添加图例
plt.scatter(x_3,y_3,label='三月份')
plt.scatter(x_10,y_10,label='10月份')
my_font=font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  #添加中文字体
plt.legend(prop=my_font)   #图例中的中文显示出来了

#添加标签
plt.xlabel('时间',fontproperties=my_font)
plt.ylabel('气温',fontproperties=my_font)
plt.title('3月份和10月份气温变化图')



