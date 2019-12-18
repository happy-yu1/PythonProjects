#因为添加中文字体时，需要找到当前电脑支持字体的路径
#C:/Windows/Fonts/simhei.ttf-----黑体
#C:/Windows/Fonts/simsun.ttc-----宋体

from  matplotlib import pyplot as plt
import  random
from matplotlib import font_manager  #font_manager用来管理字体样式，
x=range(11,20)
y1=[1,0,3,4,5,2,9,10,3]
y2=[2,1,2,0,3,5,4,4,7]

my_font=font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  #添加中文字体
plt.figure(figsize=(20,8),dpi=90)
plt.plot(x,y1,label='我的y1')
plt.plot(x,y2,label='你的y2')
plt.legend(prop=my_font)   #图例中的中文显示出来了
# plt.show()
print(help(plt.legend))
'''
通过设置 loc参数，改变图例的位置
        'best'            0
        'upper right'     1
        'upper left'      2
        'lower left'      3
        'lower right'     4
        ……
'''