from  matplotlib import pyplot as plt
import  random
from matplotlib import font_manager

x = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
y_1 = [15746,312,4497,319]
y_2 = [12357,156,2045,168]
y_3 = [2358,399,2358,362]

t=0.2
x_1=range(len(x))
x_2= [i+t for i in x_1]
x_3= [i+t*2 for i in x_1]

p_1=[y_1[i]/(y_1[i]+y_2[i]+y_3[i]) for i in range(len(x))]  # y_1的频率
p_2=[y_2[i]/(y_1[i]+y_2[i]+y_3[i]) for i in range(len(x))]  # y_2的频率
p_3=[y_3[i]/(y_1[i]+y_2[i]+y_3[i]) for i in range(len(x))]  # y_3的频率

plt.figure(figsize=(20,8),dpi=90)
plt.bar(x_1,p_1,width=t,label='第一天')
plt.bar(x_2,p_2,width=t,label='第二天')
plt.bar(x_3,p_3,width=t,label='第三天')

my_font=font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
plt.legend(prop=my_font)

plt.xticks(x_2,x,fontproperties=my_font)
plt.xlabel('电影',fontproperties=my_font)
plt.ylabel('票房频率',fontproperties=my_font)
plt.title('频率统计图',fontproperties=my_font)
