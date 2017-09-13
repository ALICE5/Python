import requests
import re
import pandas as pd
import json
from datetime import date

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

# print(dji_df.last_trade.mean())
# print(dji_df[dji_df.last_trade>=180].name)


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

# 统计美国运通公司近一年股票涨和跌分别的天数
# print(len(quotesdf[quotesdf.close>quotesdf.open]))
# print(len(quotesdf)-127)
# print(len(quotesdf[quotesdf.close<quotesdf.open]))

# 统计美国运通公司近一年相邻两天收盘价的涨跌情况
# import numpy as np
# status = np.sign(np.diff(quotesdf.close)) # sign取符号
# print(status)
# print(status[np.where(status==1)].size)
# print(status[np.where(status==-1)].size)

# 排序：按最近一次成交价对30只道指成分股股票进行排序 并列出前三甲公司名
# tempdf = dji_df.sort_values(by='last_trade',ascending=False)
# print(tempdf)
# print(tempdf[:3].name)

# 统计本年度1月份的股票开盘天数
# t = quotesdf[(quotesdf.index >= '2017-01-01')&(quotesdf.index<'2017-02-01')]
# print(len(t))

# 统计近一年每个月的股票开盘天数
import time
listtemp = []
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i],"%Y-%m-%d")
    listtemp.append(temp.tm_mon)
tempdf = quotesdf.copy()
tempdf['month'] = listtemp # 向dataframe中插入month列
print(tempdf['month'].value_counts())

