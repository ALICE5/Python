# 'b_' 默认样式

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

x = closeMeansKO.index
y = closeMeansKO.values
# plt.subplot(211)
# plt.plot(x,y,color='r',marker='o')
plt.axes([.1,.1,0.8,0.8])
plt.plot(x,y,color='green',marker='o')
# plt.plot(closeMeansKO)
# plt.plot(x, y,'g*')
# plt.title('Stock Statistics of Coca-cola')
# plt.xlabel('Month')
# plt.ylabel('Average Close Price')
# plt.show()
# help(plt.plot)


# import pylab as pl
# import numpy as np
# pl.figure(figsize=(8,6),dpi=100) # 图的大小和精度
# t = np.arange(0.,4.,0.1)
# pl.plot(t,t,color='red',linestyle='-',linewidth=3,label='Line1')
# pl.plot(t,t+2,color='green',linestyle='',marker='*',linewidth=3,label='Line2')
# pl.plot(t,t**2,color='blue',linestyle='',marker='+',linewidth=3,label='Line3')
# pl.legend(loc='upper left') # 指定图例的位置 图例的内容由label确定
# pl.show()


# 多子图 - subplots
quotes = retrieve_quotes_historical('IBM')
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
closeMeansIBM = tempdf.groupby('month').close.mean()
xi = closeMeansIBM.index
yi = closeMeansIBM.values
# plt.subplot(212)
# plt.plot(xi,yi,color='green',marker='o')
plt.axes([.3,.15,0.4,0.3])
plt.plot(xi,yi,color='red',marker='o')
plt.show()