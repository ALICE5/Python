# Series 有序定长的字典 index和value之间是独立的
# 类似一维数组的对象；由数据和索引组成
import pandas as pd
from pandas import Series
aSer = pd.Series([1,2.0,'a'])
print(aSer)

bSer = pd.Series(['apple','peach','lemon'],index=[1,2,3])
print(bSer)
print(bSer.index)
print(bSer.values)

aSer = Series([3,5,7],index=['a','b','c'])
print(aSer['b'])
print(aSer * 2)

import numpy as np
print(np.exp(aSer))

# Series 数据对齐
data = {'AXP':'86.40','CSCO':'122.64','BA':'99.44'}
sindax = ['AXP','CSCO','BA','AAPL']
aSer = pd.Series(data,index=sindax)
print(aSer)
print(pd.isnull(aSer))

bSer = {'AXP':'86.40','CSCO':'122.64','CVX':'23.78'}
cSer = pd.Series(bSer)
print(aSer+cSer)

aSer.name = 'cnames'
aSer.index.name = 'volume'
print(aSer)

