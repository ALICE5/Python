dict = {'1':'a','2':'a'}
print(dict['1'],dict['2'])
print(sorted(set('You need Python.')))

dict_mark_1 = {'Wang': 98, 'Li': 87, 'Ma': 93}
dict_mark_2 = {'Li': 90, 'Ma': 95, 'Xu': 75}
dict_mark_1.update(dict_mark_2)
print(dict_mark_1.pop('Li'))

a = {1, 2, 3, 4}
b = {2, 3, 5, 6}
print(a.difference(b) == a - b)
print(a.union(b) == a | b)
print( a.intersection(b) == a & b)

import numpy as np
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(a[[2]].sum())

from pandas import Series
sa = Series(['a', 'b', 'c'], index=[0, 1, 2])
sb = Series(['a', 'b', 'c'])
sc = Series(['a', 'c', 'b'])
print(sa.equals(sc))
print(sb.equals(sa))

from pandas import Series, DataFrame
data = {'language': ['Java', 'PHP', 'Python', 'R', 'C#'],
        'year': [ 1995 ,  1995 , 1991   ,1993, 2000]}
frame = DataFrame(data)
frame['IDE'] = Series(['Intellij', 'Notepad', 'IPython', 'R studio', 'VS'])
print('VS' in frame['IDE'].values)
print(frame['year'][2])

color = {"色彩":[
    	          {"暖色":["红","橙","黄"]},
                {"冷色":["青","蓝"]},
                {"中性色":["紫","绿","黑","灰","白"]}
        ]}
print(color['色彩'][1]['冷色'])

def find_person(dict_users, strU):
    if strU in dict_users.keys():
        return dict_users[strU]
    else:
        return 'Not Found'
if __name__ == "__main__":
     dict_users = {'xiaoyun':88888,'xiaohong':5555555,'xiaoteng':11111,'xiaoyi':12341234,'xiaoyang':1212121}
     strU =  input('Please input the name: ')
     print(find_person(dict_users,strU))

