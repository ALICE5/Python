# 数据选择：选择行、选择列、选择区域、筛选（条件选择）
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
# print(quotesdf)

# 选择行：切片、索引
# print(quotesdf['2017-05-01':'2017-05-05'])

# 选择列：列名
# print(quotesdf['open'])
# print(quotesdf.open)

# 多列选择：标签label（loc）
# print(quotesdf.loc['2017-05-01':'2017-05-05',]) # 指定行、列的索引
# print(quotesdf.loc[:,['close','open']])
# print(quotesdf.loc['2017-05-01':'2017-05-05',['open','close']])

# 单个值：at
# print(quotesdf.loc['2017-05-01','close'])
# print(quotesdf.at['2017-05-01','close'])

# 行、列和区域：iloc（物理位置） 取某个值：iat
# print(quotesdf.loc['2017-05-01':'2017-05-05',['open','close']])
# print(quotesdf.iloc[1:6,[3,0]])
#
# print(quotesdf.loc['2017-05-01','open'])
# print(quotesdf.at['2017-05-01','open'])
# print(quotesdf.iloc[0,3])
# print(quotesdf.iat[0,3])

# 条件筛选
# 三月份股票信息
print(quotesdf[(quotesdf.index>='2017-03-01')&(quotesdf.index<='2017-03-31')])
print(quotesdf[(quotesdf.index>='2017-01-01')&(quotesdf.index<='2017-03-31')&(quotesdf.close>=80)])