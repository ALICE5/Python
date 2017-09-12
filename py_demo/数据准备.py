import requests
import re
import pandas as pd
import json

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
# print(dji_df)

cols = ['code','name','last_trade']
dji_df.columns =cols
dji_df.index = range(1,len(dji_df)+1)
print(dji_df)


from datetime import date
firstday = date.fromtimestamp(1464010200)
lastday = date.fromtimestamp(1495200600)
print(firstday)
print(lastday)


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
print(quotesdf)

import pandas as pd
dates = pd.date_range('20170520',periods=7)
print(dates)

import numpy as np
datesdf = pd.DataFrame(np.random.randn(7,3),index = dates,columns=list('ABC'))
print(datesdf)