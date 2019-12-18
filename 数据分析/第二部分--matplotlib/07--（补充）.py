from  matplotlib import pyplot as plt
import numpy as np
import matplotlib
import matplotlib.dates as mdates
import datetime
from matplotlib import font_manager
import csv,random

# N=1000
# x=np.random.randn(N)   #随机生成1000个标准正太分布的数据
# y=np.random.randn(N)
#
# plt.scatter(x,y,)
# # print(help(matplotlib.markers))
# x=np.linspace(-10,10,100)
# y=x**2
# plt.plot(x,y)
header=['date','temper']
x = ['10/{}/2015'.format(i) for i in range(1,32)]+['11/{}/2015'.format(i) for i in range(1,31)]
# x = ['10月{}日'.format(i) for i in range(1,32)]+['11月{}日'.format(i) for i in range(1,31)]
y=[random.randint(20,35) for i in range(61)]
totle=[(x[i],y[i]) for i in range(61)]
# for i in totle:
#     for n in i:
#         print(type(n))
#         break
with open('temper.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(totle)

def datestr2num(bytedate):
    return datetime.datetime.strptime(bytedate.decode('utf-8'),'%m/%d/%Y')

date,y=np.loadtxt('temper.csv',delimiter=',',converters={0:datestr2num},skiprows=1,usecols=(0,1))
# print(date)


# date=np.loadtxt('temper.csv',delimiter=',',converters={0:mdates.datestr2num('%m/%d/%Y')},skiprows=1,usecols=(0))

# date=np.loadtxt('temper.csv',delimiter=',',skiprows=1,usecols=(0))
# print(date)  Use time.strptime or dateutil.parser.parse or datestr2num instead


# date=np.loadtxt('temper.csv',delimiter=',',dtype=float,converters={0: mdates.time.strptime(i,str(['%m/%d/%Y' for i in x]))},skiprows=1,usecols=(0))

# with open('temper.csv','r') as f:
#     reader=csv.reader(f)
#     for i in reader:
#         print(i[0])   #通过下标的方式读取到日期