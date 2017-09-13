# 分组

import requests
import re
import pandas as pd
import json
from datetime import date

def retrieve_quotes_historical(stock_code):
    quotes =[]
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code,stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"',r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('AXP')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date']) # 转换成常规时间
    y = date.strftime(x,'%Y-%m-%d') # 转换成固定格式
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes,index=list1)
quotesdf_m = quotesdf_ori.drop(['adjclose'],axis=1) # 删除adjclose列
quotesdf = quotesdf_m.drop(['date'],axis=1) # 删除原date列

import time
listtemp = []
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i],"%Y-%m-%d")
    listtemp.append(temp.tm_mon)
tempdf = quotesdf.copy()
tempdf['month'] = listtemp # 向dataframe中插入month列

# 统计近一年每个月的股票开盘天数
# x = tempdf.groupby('month').count()
# print(x)
# print(x.close)

# 统计近一年每个月的总成交量
# print(tempdf.groupby('month').sum().volume)
# min max mean

# 高效处理
# print(tempdf)
print(tempdf.groupby('month').volume.sum())