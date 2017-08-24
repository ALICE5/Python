# list 实现映射
names = ['Wangdachui','Niuyun', 'Linling','Tianqi']
salaries = [3000, 2000, 4500, 8000]
print(salaries[names.index('Niuyun')])

# dict
aInfo = {'Wangdachui':3000, 'Niuyun':2000, 'Linling':4500, 'Tianqi':8000}
info = [('Wangdachui',3000),('Niuyun',2000),('Linling',4500),('Tianqi',8000)]
bInfo = dict(info)
cInfo = dict([['Wangdachui',3000],['Niuyun',2000],['Linling',4500],['Tianqi',8000]])
dInfo = dict(Wangdachui = 3000, Niuyun = 2000, Linling = 4500, Tianqi = 8000)
eInfo = dict((('Wangdachui',3000),('Niuyun',2000),('Linling',4500),('Tianqi',8000)))
print(aInfo)
print(bInfo)
print(cInfo)
print(dInfo)
print(eInfo)

# 设置默认工资为3000
aDict = {}.fromkeys(('Wangdachui','Niuyun','Linling','Tianqi'),3000)
# fromkeys的第一个元素只要是序列即可 但不可变
print(aDict)
print(sorted(aDict)) # 返回key内部的存储顺序

# 已有姓名列表和工资列表 生成字典
names = ['Wangdachui','Niuyun', 'Linling','Tianqi']
salaries = [3000, 2000, 4500, 8000]
dz = dict(zip(names,salaries))
print(dz)

# 由现有数据生成字典
pList = [('AXP','American Express Company','78.51'),
      ('BA','The Boeing Company','184.76'),
      ('CAT','Caterpillar Inc.','96.39'),
      ('CSCO','Cisco Systems Inc.','33.71'),
      ('CVX','Chevron Corporation','106.09')]
aList = []
bList = []
for i in range(5):
    aStr = pList[i][0]
    bStr = pList[i][2]
    aList.append(aStr)
    bList.append(bStr)
aDict = dict(zip(aList,bList))
print(aDict)

# 字典的基本操作
aInfo = {'Wangdachui':3000, 'Niuyun':2000, 'Linling':4500, 'Tianqi':8000}
print(aInfo['Niuyun'])
aInfo['Niuyun'] = 9999
print(aInfo)
aInfo['Fuyun'] = 1000
print(aInfo)
print('Mayun' in aInfo)
del aInfo['Fuyun']
print(aInfo)

# 字典的内建函数
names = ['Wangdachui','Niuyun', 'Linling','Tianqi']
salaries = [3000, 2000, 4500, 8000]
aInfo = dict(zip(names,salaries))
print(aInfo,len(aInfo))
print(hash('Wangdachui')) # 判断对象是否可哈希(可变) 若可哈希(不可变) 则出现哈希值
print(aInfo.keys())
print(aInfo.values())
print(aInfo.items())
for k,v in aInfo.items():
    print(k,v)

# 两份人员和工资信息表：1原有信息 2更改信息和新进人员信息
aInfo = {'Wangdachui':3000, 'Niuyun':2000, 'Linling':4500, 'Tianqi':8000}
bInfo = {'Wangdachui':4000, 'Niuyun':9999,'Wangzi':6000}
aInfo.update(bInfo)
print(aInfo)

stock = {'AXP':78.51,'BA':184.76}
# print(stock['AAA']) 报错
print(stock.get('AAA')) # 返回空

# 字典删除
aStock = {'AXP':78.51,'BA':184.76}
bStock = aStock
# aStock = {}
# print(bStock)
aStock.clear()
print(aStock,bStock) # 清空原始对象 + 赋值引用的对象

aStock = {'AXP':78.51,'BA':184.76}
aStock.pop('BA') # 指定键key 而不是索引
print(aStock)

# JSON格式
x = {"name":"niuyun","adress":{"city":"beijing","street":"chaoyang road"}}
# x为json语句
print(x['adress']['street'])

# 搜索引擎关键字查询  *** 重要 ***
import requests
kw = {'q':'Python dict'}
r = requests.get('http://cn.bing.com/search',params=kw)
print(r.text)
print(r.url)

# 可变长关键字参数
def func(args1,*argst,**kwargs):
    print(args1)
    print(argst)
    print(kwargs)
func('Hello','alice','sam','lily',a1=1,a2=2,a3=3)