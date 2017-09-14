# 主要用于二维绘图 绘图API--pylot 集成库--pylab
import requests
import re
import json
import pandas as pd
from datetime import date
import time
import matplotlib.pyplot as plt

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('KO')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = list1)
quotesdf = quotesdf_ori.drop(['date'], axis = 1)
listtemp = []
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i],"%Y-%m-%d")
    listtemp.append(temp.tm_mon)
tempdf = quotesdf.copy()
tempdf['month'] = listtemp

closeMeansKO = tempdf.groupby('month').close.mean()
# print(closeMeansKO)
x = closeMeansKO.index
y = closeMeansKO.values
# plt.plot(x,y)
# plt.plot(x, y,'rD')
# plt.plot(x, y,'g--')
# plt.show()
# plt.savefig('1.jpg')


# # 折线图
# import numpy as np
# import matplotlib.pyplot as plt
# t = np.arange(0.,4.,0.1)
# plt.plot(t,t,t,t+2,t,t**2)
# plt.show()


# 散点图
# 可口可乐公司近一年来股票收盘价的月平均价绘制散点图
# plt.plot(x,y,'o')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 1) # 50个点？
# y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
# plt.plot(x, y,'o')
# plt.show()

# 柱状图
# plt.bar(x,y)
# plt.show()

# 直方图、饼图等等....


# pylab绘图：pylab中主要包含了pyplot和numpy里面的一些常用函数
# import numpy as np
# import pylab as pl
# t = np.arange(0.,4.,0.1)
# pl.plot(t,t,t,t+2,t,t**2)
# pl.show()

import numpy as np
import pylab as pl
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
pl.plot(x,y)
pl.show()