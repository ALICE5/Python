from sklearn import datasets,neighbors
iris = datasets.load_iris()
# print(iris.data)
# print(iris.data.shape) # 数据大小
# print(iris.target) # 数据所属种类

# 利用KNN分类算法进行分类
knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data,iris.target) # 从已有数据中学习
result = knn.predict([[5.0,3.0,5.0,2.0]]) # 利用分类模型进行未知数据的预测
print(result)

# 利用K-means聚类算法进行聚类
from sklearn import cluster,datasets
iris = datasets.load_iris()
kmeans = cluster.KMeans(n_clusters=3).fit(iris.data)
pred = kmeans.predict(iris.data) # 确定数据类别
for label in pred:
    print(label,end=' ')
print('\n')
for label in  iris.target:
    print(label,end=' ')

from sklearn import svm,datasets
iris = datasets.load_iris()
svc = svm.LinearSVC()
svc.fit(iris.data,iris.target) # 学习
svc.predict([[5.0,3.0,5.0,2.0]]) # 预测
