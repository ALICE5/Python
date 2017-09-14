# K-均值算法：简洁、快速
import numpy as np
from scipy.cluster.vq import vq,kmeans,whiten
list1 = [88.0,74.0,96.0,85.0]
list2 = [92.0,99.0,95.0,94.0]
list3 = [91.0,87.0,99.0,95.0]
list4 = [78.0,99.0,97.0,81.0]
list5 = [88.0,78.0,98.0,84.0]
list6 = [100.0,95.0,100.0,92.0]
data = np.array([list1,list2,list3,list4,list5,list6])
# print(data)
whiten = whiten(data) # 计算各列元素的标准差 形成新的数组
# print(whiten)
centroids,_ = kmeans(whiten,2) # kmeans对数据进行聚类 这里分为2类
# 返回结果是元组 只需要第一个值
# print(kmeans(whiten,2))
# print(centroids)
result,_ = vq(whiten,centroids) # vq矢量量化函数 对每个数据进行归类
print(result)



# Scikit-learn 开源机器学习模块 提供了各种机器学习算法的接口
import numpy as np
from sklearn.cluster import KMeans
list1 = [88.0,74.0,96.0,85.0]
list2 = [92.0,99.0,95.0,94.0]
list3 = [91.0,87.0,99.0,95.0]
list4 = [78.0,99.0,97.0,81.0]
list5 = [88.0,78.0,98.0,84.0]
list6 = [100.0,95.0,100.0,92.0]
X = np.array([list1,list2,list3,list4,list5,list6])
kmeans = KMeans(n_clusters=2).fit(X) # fit 对KMeans确定类别之后的数据集 进行聚类
pred = kmeans.predict(X) # predict 根据聚类对结果确定数据所属的类别
print(pred)



# 分类：训练集、测试集
from sklearn import datasets
from sklearn import svm
clf = svm.SVC(gamma=0.001,C=100.)
digits = datasets.load_digits()
clf.fit(digits.data[:-1],digits.target[:-1])
result = clf.predict([digits.data[-1]])
print(result)



# 基于10只道指成分股近一年相邻两天的收盘价涨跌数据规律对它们进行聚类
import requests
import re
import json
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

def create_df(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    list1 = ['close','date','high','low','open','volume']
    df_totalvolume = pd.DataFrame(quotes,columns=list1)
    return df_totalvolume

listDji = ['MMM','AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS']
listTemp = [0] * len(listDji)
for i in range(len(listTemp)):
    listTemp[i] = create_df(listDji[i]).close
status = [0] * len(listDji)
for i in range(len(status)):
    status[i] = np.sign(np.diff(listTemp[i]))
kmeans = KMeans(n_clusters = 3).fit(status)
pred=kmeans.predict(status)
print(pred)
