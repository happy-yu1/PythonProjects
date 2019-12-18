
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
#初始化
pro=ts.pro_api('5f2dc9d17ebed3601a4fbea74148a25067d067138bf88515693e9b7d')
df=pro.stock_basic()

t=pd.DataFrame(np.random.randint(1,100,12).reshape(3,4),index=list('acb'),columns=list('ACDB'))
d=pd.Series(np.random.randint(1,100,5),index=list('abcde'))

d.argmax()

