# 剔除重复的员工信息
names = ['Wangdachui','Niuyun','Wangzi','Linling','Niuyun']
namesSet = set(names)
print(namesSet)

# 集合: 一个无序不重复的元素的组合 1可变集合 2不可变集合
aSet = set('hello')
print(aSet)
bSet = frozenset('hello') # 不可变集合
print(bSet)
print(type(aSet),type(bSet))

# 集合比较: < <= > >=都是指包含关系 分别为真子集 子集 真子集 子集
aSet = set('sunrise')
bSet = set('sunset')
print('u' in aSet)
print(aSet == bSet) # 判断成员是否相同
print(aSet < bSet)  # 包含关系 aset是不是bset的真子集
print(set('sun')<aSet) # < <= > >=都是指包含关系

# &: 交集  |: 并集  -: 差集  ^: 异或
aSet = set('sunrise')
bSet = set('sunset')
print(aSet&bSet)
print(aSet|bSet)
print(aSet-bSet) # 属于a 但不属于b
print(aSet^bSet) # 对称差分: 属于a 或属于b 但都是单独属于 不同时
aSet -= set('sun') # 运算符可符合: &= |= -= ^=
print(aSet)

# 集合内建函数
aSet = set('sunrise')
bSet = set('sunset')
print(aSet.issubset(bSet))
print(aSet.issubset('sunrises'))
print(aSet.intersection(bSet)) # 交集
print(aSet.difference(bSet)) # 差补
cSet = aSet.copy()
print(cSet,aSet)

aSet.add('!')
print(aSet)
aSet.remove('!')
print(aSet)
aSet.update('Yeah') # 扩充
print(aSet)
aSet.clear()
print(aSet)







