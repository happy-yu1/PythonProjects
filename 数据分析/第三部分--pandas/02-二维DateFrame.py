
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient



#
# print(t)
# print(t.dtypes)
# b={'name':['z3','li4','w5'],'age':[23,16,27],'socre':[78,81,48]}
# t=pd.read_csv('trainx.csv')
# date=pd.DataFrame(t)
#
# print(date)
# print(type(date))  #  pandas.core.frame.DataFrame

a=[{'name':'z3','age':23,'socre':78},
   {'name':'li4','age':16,'socre':81},
   {'name':'w5','age':27,'socre':48}]

t=pd.DataFrame(np.arange(12).reshape(3,4))
t.sort_index()