import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
from pymongo import MongoClient
t=pd.Series([1,2,3],index=list('abc'))    #dtype: int64
print(t)

a={'name':'zhang3','age':23,'socre':78}
a1={string.ascii_uppercase[i]:i for i in range(3)}
b=pd.Series(a1)
