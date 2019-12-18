#一、导入datetime包
# import datetime
# print(datetime.date(2019, 3, 20))  # 提供year，month，day属性
# # print(datetime.date(2019, 3, 20).day)
# print(datetime.time(3,30,10))  #提供hour，minute，second，microsecond等属性
# print(datetime.time(3,30,10).second)

# from datetime import  time
# t=time(3,30,10)  #等于import datetime时 t=datetime.time(3,30,10)
# print(t.second)

#二、从datetime包中导入datetime模块
# from datetime import datetime

#
# print(datetime(2018,9,18).today())
# print(datetime(2018,9,18).now())

# 三、从datetime包中导入timedelta模块：提供时间差的功能
from datetime import datetime,timedelta
print(datetime(2018,9,18).now())
tn=datetime.now()
print(tn.strftime('%Y-%m-%d %H:%M:%S'))

print('----1-----')

td=timedelta(hours=1)  #表示产生一个小时的时间差
print((tn+td).strftime('%Y-%m-%d %H:%M:%S'))
print((tn-td).strftime('%Y-%m-%d %H:%M:%S'))

ts=timedelta(seconds=20)
print((tn+ts).strftime('%Y-%m-%d %H:%M:%S'))

print('---2----')
import  time
def func():
    time.sleep(3.5)  #暂停3.5秒
t1=time.time()   #计算时间戳
func()
print((time.time()-t1))  #判断程勋运行时间是多少  结果：3.5002002716064453