import numpy as np
aArray = np.ones((3,4))
print(aArray)

# 线性代数运算 -- 计算行列式
from scipy import linalg
arr = np.array([[1,2],[3,4]])
print(linalg.det(arr))

# ndarray : NumPy中基本的数据类型 所有元素都是同一种类型 节省内存和CPU计算时间 丰富的函数
import numpy as np
aArray = np.array([1,2,3])
print(aArray)
bArray = np.array([(1,2,3),(4,5,6)])
print(bArray)

print(np.arange(1,5,0.5))
print(np.random.random((2,2)))
print(np.linspace(1,2,10,endpoint=False))

print(np.ones([2,3]))
print(np.zeros((2,2)))
print(np.fromfunction(lambda i,j:(i+1)*(j+1),(9,9)))

import numpy as py
x = np.array([(1,2,3),(4,5,6)])
print(x)
print(x.ndim)
print(x.shape)
print(x.size)
y = np.arange(1,10,0.5)
print(y)

a = np.arange(1,5)
print(np.power(a,2).sum())
# power 是平方 然后 求和
print(np.add(a,np.arange(4)))

aArray = np.array([(1,2,3),(4,5,6)])
print(aArray[1])
print(aArray[0:2])
print(aArray[:,[0,1]]) # 行全要 列要0和1列
print(aArray[1,[0,1]])
for row in aArray:
    print(row)
print(aArray.shape)

bArray = aArray.reshape(3,2)
print(bArray)
print(bArray.shape) # 并不改变aArray的形式

aArray.resize(3,2)
print(aArray) # 真正改变aArray的形式
bArray = np.array([1,3,7])
cArray = np.array([3,5,8])
print(np.vstack((bArray,cArray))) # 在垂直方向拼接
print(np.hstack((bArray,cArray))) # 在水平方向拼接

aArray = np.array([(5,5,5),(5,5,5)])
bArray = np.array([(2,2,2),(2,2,2)])
cArray = aArray * bArray
print(cArray)
aArray += bArray
print(aArray)

a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])
print(a+b)

aArray = np.array([(1,2,3),(4,5,6)])
print(aArray.sum())
print(aArray.sum(axis=0))
print(aArray.sum(axis=1))
print(aArray.min())
print(aArray.argmax()) # 返回最大值的索引
print(aArray.mean()) # 返回平均值
print(aArray.var()) # 方差
print(aArray.std()) # 标准差

import numpy as np
x = np.array([[1,2],[3,4]])
r1 = np.linalg.det(x) # 行列式
print(r1)
r2 = np.linalg.inv(x) # 逆矩阵
print(r2)
r3 = np.dot(x,x) # 矩阵内积
print(r3)





