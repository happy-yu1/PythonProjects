import time
import calendar
print(time.time()) #输出从1970年1月1日0时0分0秒到现在的秒数，32位的系统最远可以到2038年
# help(time.time)
print(time.timezone)  #输出当前时区和世界时区相差的秒数，为一个固定值
# help(time.timezone)

print(time.altzone)
# help(time.daylight)

# print(time.localtime()) #输出当前时间结构
# t=time.localtime()
# print(time.asctime(t)) #将获得的时间结构字符串化

# print(time.ctime())  #  直接获得字符串化的当前时间
# t=time.localtime()
# st=time.strftime(('%Y-%m-%d %H:%M'),(t))  #以自己想要的格式展现出当前时间,一定要以元组的形式表现出来
#和datetime模块中的strftime调用方法不同  datetime.now().strftime('%Y-%m-%d %H:%M')
# print(st)
# print(t
# help(time.strftime) #会出来该函数下对应的格式和含义如：%d表示一个月中的第几天
