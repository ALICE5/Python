import requests
import re
import pandas as pd

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*<span.*">(.*?)<\/span>.*\n.*class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern,r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append([item[0],item[1],float(item[2])]) # 转成float类型
    return dji_list

dji_list = retrieve_dji_list()
dji_df = pd.DataFrame(dji_list)

cols = ['code','name','last_trade']
dji_df.columns =cols
dji_df.index = range(1,len(dji_df)+1)
# print(dji_df)
#
# print(dji_df.index)
# print(dji_df.columns)
# print(dji_df.values)
# print(dji_df.describe())

print(dji_df.last_trade) # float64

print(dji_df.head(5)) # 行显示 前5个 dji_df[:5]
print(dji_df.tail(5)) # 行显示 后5个 dji_df[-5:]

print(dji_df.last_trade) # 列显示

print(dji_df.shape) # 维度
print(dji_df.size) # 数据个数