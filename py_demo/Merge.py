# 连接：append concat join

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

# 把美国运通公司本年度1月1日至1月5日间的股票交易信息合并到近一年中前两天的股票信息中
# p = quotesdf[:2] # 前两天
# print(p)
# q = quotesdf['2017-01-01':'2017-01-05']
# print(q)
# print(p.append(q))
# 追加

# 将美国运通公司近一年股票数据中的前5个和后5个合并
# pieces = [quotesdf[:5],quotesdf[len(quotesdf)-5:]]
# print(pd.concat(pieces))
# 连接

# 两个不同逻辑结构的对象能否连接：ignore_index
# pieces1 = quotesdf[:3]
# pieces2 = tempdf[:3]
# x = pd.concat([pieces1,pieces2],ignore_index=True)
# print(x)

# 将美国运通公司和可口可乐公司一年中的每个月的交易总量表与30只道琼斯成分股股票信息合并
AKdf = pd.DataFrame(tempdf.groupby('month').volume.sum())
AKdf['code'] = ['AXP'] * 12
AKdf['month'] = range(1,13)
# print(AKdf)

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*<span.*">(.*?)<\/span>.*\n.*class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern,r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append([item[0],item[1],float(item[2])])
    return dji_list

dji_list = retrieve_dji_list()
dji_df = pd.DataFrame(dji_list)

cols = ['code','name','last_trade']
dji_df.columns =cols
dji_df.index = range(1,len(dji_df)+1)

mgdf = pd.merge(dji_df.drop(['last_trade'],axis=1),AKdf,on='code')
print(mgdf)

# merge函数的参数：left right how on copy sort left_on right_on .....