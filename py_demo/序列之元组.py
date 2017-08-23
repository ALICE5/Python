# 元组
bTuple = (['Monday',1],2,3)
print(bTuple)
print(bTuple[0][0])
print(len(bTuple))
print(bTuple[1:])
cTuple = (24)
print(cTuple)
cTuple= (24,) # 创建一个元素的Tuple
print(cTuple)

# 列表的元素可变 元组的元素不可变
aList = ['AXP','BA','CAT']
aTuple = ('AXP','BA','CAT')
aList[1] = 'Alibaba'
print(aList)
# aTuple[1] = 'Alibaba' 报错
# print(aTuple)
a = [3,5,2,4]
b = sorted(a) # 创建副本 原始列表未改变
print(b)
print(a)
a.sort() # 原始列表改变
print(a)
c = (3,5,2,4)
d = sorted(c)
print(d)
print(c)
# c.sort() 报错

# 元组可以: 1在映射类型中当作键使用 2函数的特殊类型参数 3作为函数的特殊返回值
def foo(args1,args2='World!'):
    print(args1,args2)
foo('Hello,')
foo('Hello,',args2='Python@')
foo(args2='Apple!',args1='Hi,')

def foo(args1, *argst): # 可变长的位置参数 -> 元组
    print(args1)
    print(argst)
foo('Hello!','Alice','Jam','Lily')

def foo(): # 函数特殊返回值 -> 元组
    return 1,2,3
print(foo())