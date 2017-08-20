import numpy as np
from scipy.cluster.vq import vq,kmeans,whiten
# k-means聚类
list1 = [88.0, 74.0, 96.0, 85.0]
list2 = [92.0, 99.0, 95.0, 94.0]
list3 = [91.0, 87.0, 99.0, 95.0]
list4 = [78.0, 99.0, 97.0, 81.0]
list5 = [88.0, 78.0, 98.0, 84.0]
list6 = [100.0, 95.0, 100.0, 92.0]
data = np.array([list1,list2,list3,list4,list5,list6])
# print(data)

whiten = whiten(data)
# 将原始数据做归一化处理

centroids,_ = kmeans(whiten,2)
# 使用kmeans函数进行聚类 输入第一维为数据 第二维为聚类个数k
# 有些时候我们可能不知道最终究竟聚成多少类
# k-means输出结果是两维的 第一维是聚类中心 第二维是损失distortion

result,_ = vq(whiten,centroids)
# 使用vq函数根据聚类中心对所有数据进行分类 vq的输出也是两维的 [0]表示的是所有数据的label
print(result)


'''
kmeans(obs, k_or_guess, iter=20, thresh=1e-05, check_finite=True) 
输入obs是数据矩阵,行代表数据数目,列代表特征维度; k_or_guess表示聚类数目;iter表示循环次数,最终返回损失最小的那一次的聚类中心; 
输出有两个,第一个是聚类中心(codebook),第二个是损失distortion,即聚类后各数据点到其聚类中心的距离的加和.
'''

'''
vq(obs, code_book, check_finite=True) 
根据聚类中心将所有数据进行分类.obs为数据,code_book则是kmeans产生的聚类中心. 
输出同样有两个:第一个是各个数据属于哪一类的label,第二个和kmeans的第二个输出是一样的,都是distortion
'''