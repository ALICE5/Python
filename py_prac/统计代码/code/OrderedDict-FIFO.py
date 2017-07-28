# -*- coding:utf-8 -*-
#OrderedDict实现FIFO的dict 容量超载时删除最早添加的key
from collections import OrderedDict
class LatUpdateOrderedDict(OrderedDict):

	def __init__(self,capacity):
		super(LatUpdateOrderedDict,self).__init__
		self._capacity = capacity

	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:',last)
		if containsKey:
			del self[key] 
			# 如果已经存在key 则删除重置
			print('set:',(key,value))
		else:
			print('add:',(key,value)) 
			# 如果不存在key 则新增
		OrderedDict.__setitem__(self,key,value) 
		    #调用父类中的赋值语句



lod = LatUpdateOrderedDict(3)
lod['a']=1
lod['b']=2
lod['c']=3
lod['a']=4
print(lod)
lod['d']=5
print(lod)