# DF对应二维表结构
import pandas as pd
import numpy as np

# 创建DataFrame
data = {'name':['Wangdachui','Linling','Niuyun'],'pay':[4000,5000,6000]}
frame = pd.DataFrame(data)
print(frame)

data = np.array([('Wangdachui',4000),('Linling',5000),('Niuyun',6000)])
frame = pd.DataFrame(data,index=range(1,4),columns=['name','pay'])
print(frame)
print(frame.index) # 行索引
print(frame.columns) # 列索引
print(frame.values) # 值

print(frame['name'])
print(frame.pay)
print(frame.iloc[:2,1]) # 行, 列

# frame['name'] = 'admin'
# print(frame)

# del frame['pay']
# print(frame)

# 找最低工资
print(frame.pay.min()) # 工资值转成了字符串

# 找高工资人群信息（>=5000）
print(frame.pay>='5000')
print(frame[frame.pay>='5000'])