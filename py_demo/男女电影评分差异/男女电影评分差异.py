# 计算MovieLens 100k数据集中男性女性用户评分的标准差并输出
import pandas as pd
unames = ['user_id','age','gender','occupation','zip_code']
users = pd.read_table('ml-100k/u.user',sep='|',header=None,names=unames,engine='python')
rnames = ['user_id','item_id','rating','timestamp']
ratings = pd.read_table('ml-100k/u.data',sep='\t',header=None,names=rnames,engine='python')
data = pd.merge(users,ratings)

mean_ratings = data.pivot_table('rating',index=['user_id','gender'],aggfunc='mean')
std = mean_ratings.groupby('gender').std()
print(std)

# mean_ratings = data.pivot_table('rating',index='user_id',columns = 'gender',aggfunc='mean')
# female_ratings = mean_ratings['F']
# female_ratings_std = female_ratings.std()
#
# male_ratings = mean_ratings['M']
# male_ratings_std = male_ratings.std()
#
# print('Gender')
# print('M %.2f' % male_ratings_std)
# print('F %.2f' % female_ratings_std)
