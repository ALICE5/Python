# csv格式数据存取
import requests
import re
import json
import pandas as pd
import numpy as np

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('AXP')
df = pd.DataFrame(quotes)
# df.to_csv('stockAXP.csv')
# 纯文本格式打开 每条记录的数据之间默认用逗号分隔

# 读csv格式数据
# result = pd.read_csv('stockAXP.csv')
# print(result['close'])


# data = np.array([['The rolling stones','Satisfaction'],['Beatles','Let it be'],
#                 ['Guns n roses','Dont cry'],['Metallica','Nothing else matters']])
# frame = pd.DataFrame(data,index=range(1,5),columns=['singer','song'])
# print(frame)
# frame.to_csv('Singer&Song.csv')

# excel数据存取
quotes1 = retrieve_quotes_historical('KO')
df1 = pd.DataFrame(quotes1)
# df1.to_excel('stockKO.xlsx',sheet_name='KO')

# df1 = pd.read_excel('stockKO.xlsx')
# print(df1['close'][:3])

# csv和excel格式的文件非常常见

data = np.array([('1001','xiaoming',77,87),
                 ('1002','xiaohong',88,82),
                 ('1003','xiaohuaa',99,91)])
frame = pd.DataFrame(data,columns=['number','name','Python','Math'])
# frame['sum_score'] = frame['Python'] + frame['Math']
templist = []
for i in range(len(frame)):
    temp = int(frame.loc[i,'Python']) + int(frame.loc[i,'Math'])
    templist.append(temp)
frame['sum_score'] = templist
print(frame)
frame.to_excel('students.xlsx',sheet_name='scores')
