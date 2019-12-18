#通过爬虫获得北京3月份和10月份每天的最低温度，画出温度随时间变化的散点图

from  matplotlib import pyplot as plt
import  random
from matplotlib import font_manager

#（1）一个x，，一个y
x = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

y=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]


#做出简单草图---中文不显示
plt.figure(figsize=(20,8),dpi=90)
my_font=font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
plt.bar(range(len(x)),y,width=0.4)

plt.show()

# 修改x刻度,并传入中文字体
plt.xticks(range(len(x)),x,fontproperties=my_font,rotation=45)

# 添加标签
plt.xlabel('电影名称',fontproperties=my_font)
plt.ylabel('票房',fontproperties=my_font)
plt.title('电影票房对比条形图',fontproperties=my_font)


# 5.3、将电影信息放在y轴上展示---barh（）横条形图
plt.figure(figsize=(20,9),dpi=90)
my_font=font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')

plt.barh(range(len(x)),y,height=0.6)   #bar----barh,width---height
plt.yticks(range(len(x)),x,fontproperties=my_font)   #xticks----yticks


plt.ylabel('电影名称',fontproperties=my_font)
plt.xlabel('票房',fontproperties=my_font)
plt.title('电影票房对比条形图',fontproperties=my_font)

# plt.show()


#（2）一个x，，多个y
#多个y时，要注意进行x轴刻度的分割，防止出现重叠的现象
x = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
y_1 = [15746,312,4497,319]
y_2 = [12357,156,2045,168]
y_3 = [2358,399,2358,362]

plt.bar(range(len(x)),y_1,width=0.4,label='第一天')
plt.bar(range(len(x)),y_2,width=0.4,label='第二天')
plt.bar(range(len(x)),y_2,width=0.4,label='第三天')

my_font=font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
plt.legend(prop=my_font)

plt.xticks(range(len(x)),x,fontproperties=my_font,rotation=45)
plt.xlabel('电影',fontproperties=my_font)
plt.ylabel('票房',fontproperties=my_font)



x_1=range(len(x))
x_2= [i+0.2 for i in x_1]
x_3= [i+0.2*2 for i in x_1]

# plt.show()