# import requests
# import re
# import json
# import pandas as pd
# from datetime import date
# import matplotlib.pyplot as plt
#
# def retrieve_quotes_historical(stock_code):
#     quotes = []
#     url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
#     r = requests.get(url)
#     m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
#     if m:
#         quotes = json.loads(m[0])
#         quotes = quotes[::-1]
#     return  [item for item in quotes if not 'type' in item]
#
# quotes = retrieve_quotes_historical('KO')
# list1 = []
# for i in range(len(quotes)):
#     x = date.fromtimestamp(quotes[i]['date'])
#     y = date.strftime(x,'%Y-%m-%d')
#     list1.append(y)
# quotesdf_ori = pd.DataFrame(quotes, index = list1)
# quotesdf = quotesdf_ori.drop(['date'], axis = 1)
#
# quotesdf.close.plot()
# plt.title('Stock Statistics of Coca-Cola')
# plt.xlabel('Month')
# plt.ylabel('Average Close Price')
# plt.show()

import requests
import re
import json
import pandas as pd
from datetime import date
import time
from pylab import *
from scipy.cluster.vq import *


def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

def create_volumes(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    list1 = []
    for i in range(len(quotes)):
        x = date.fromtimestamp(quotes[i]['date'])
        y = date.strftime(x,'%Y-%m-%d')
        list1.append(y)
    quotesdf_ori = pd.DataFrame(quotes, index = list1)
    listtemp = []
    for i in range(len(quotesdf_ori)):
        temp = time.strptime(quotesdf_ori.index[i],"%Y-%m-%d")
        listtemp.append(temp.tm_mon)
    tempdf = quotesdf_ori.copy()
    tempdf['month'] = listtemp
    totalvolume = tempdf.groupby('month').volume.sum()
    return totalvolume

INTC_volumes = create_volumes('INTC')
IBM_volumes = create_volumes('IBM')
# print(INTC_volumes)
# print(IBM_volumes)
quotesIIdf = pd.DataFrame()
quotesIIdf['INTC'] = INTC_volumes
quotesIIdf['IBM'] = IBM_volumes
# quotesIIdf.plot(kind='bar',stacked=True)
# quotesIIdf.plot(kind='barh')
# quotesIIdf.plot(marker='v')
quotesIIdf.boxplot()
# 箱形图： 1-最大值  2-第一个四分位数（25%） 3-中位数（50%） 4-75%  5-最小值
# 可能还有一些异常值
plt.show()

# quotesINTC = INTC_volumes[0:3]
# print(quotesINTC)
# quotesINTC.plot(kind='pie',subplots=True,autopct='%.2f')
# plt.show()


