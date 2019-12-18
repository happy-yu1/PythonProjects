
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient
'''
# 用cd命令打开mongod.exe所在的目录，并输入mongod.exe --nojournal --dbpath .（注意–dbpath后面有个点） 
# MongoDB数据库常用的三种命令
# - mongod.exe --nojournal --dbpath #以控制台方式启动服务器 
# - mongod.exe --install #安装MongoDB以服务方式运行 
# - mongod.exe --help #显示所有的命令选项
'''
client=MongoClient(host="localhost",port=27017)
# print(client.address)
collecton=client['test']['students']

# students={'name':['z3','li4','w5'],'age':[23,16,27],'socre':[78,81,48]}
students=[{'name':'women--','age':23,'socre':78},
   {'name':'li4','age':16,'socre':81},
   {'name':'w5','age':27,'socre':48}]

result=collecton.insert_many(students)

# date=list(collecton.find())
# print(date)
print(list(collecton.find({'name':'w5'})))



# t=pd.read_csv('trainx.csv')
# print(t,t.dtypes,t.shape)
