# 数据收集 数据整理 数据描述 数据分析
# 本地数据：文件打开、读写、关闭
# 网络数据：抓取 - urllib内建模块、Request第三方库、Scrapy框架
#          解析 - BeautifulSoup库、re模块

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
print(dji_df)

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
quotesdf = pd.DataFrame(quotes)
print(quotesdf)


# 豆瓣API 返回Json格式的数据 无须解析
import requests
r = requests.get('https://api.douban.com/v2/book/1084336')
print(r.text)


import requests
r = requests.get('https://api.douban.com/v2/movie/subject/1291546')
data = r.json()
print(data['title'],data['rating']['average'])


import nltk
# nltk.download()
from nltk.corpus import gutenberg
print(gutenberg.fileids())
texts = gutenberg.words('shakespeare-hamlet.txt')
print(texts)

