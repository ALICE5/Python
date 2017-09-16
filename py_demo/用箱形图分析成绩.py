# 箱形图 是一种用作显示一组数据分散情况资料的统计图
import pandas as pd
import matplotlib.pylab as plt
scores = pd.read_excel('score.xlsx')
scores.boxplot()
plt.show()

# 问题分析
#（1）Math、Python、Chemisty分布比较集中；English、PE分布比较分散（箱子长度）
#（2）Python分布最均匀；PE分布最不均匀（中位数到上下四分位的距离）
#（3）Python总体情况最好；Math、English、Music的总体情况不好（中位数的位置）
#（4）Maths、Python和Physics中分别有2个、1个、1个异常值（离群点）