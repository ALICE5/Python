# 列表
aList = list('Hello.')
print(aList)
aList[0]='h'
print(aList)
bList = [1,2,'a',3.5]
print(bList)

# 校园歌手比赛 评委打分+观众打分
jScores = [9,9,8.5,10,7,8,8,9,8,10]
aScore = 9
jScores.sort()
jScores.pop()
jScores.pop(0)
jScores.append(aScore)
print(jScores)
aveScore = sum(jScores) / len(jScores)
print(aveScore)

# 将工作日与周末的表示形式合并
week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend = ['Saturday','Sunday']
week.extend(weekend)
# week.append(weekend)
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ['Saturday', 'Sunday']]
print(week)
for i,j in enumerate(week):
    print(i+1,j)

# 根据列表元素的长度进行排序
list1 = ['aa','a','aaaaa','vvv']
list1.sort(key=len)
print(list1)
list1.sort(key=len,reverse=True)
print(list1)

# 列表解析
l1 = [x for x in range(10)]
print(l1)
l2 = [x ** 2 for x in range(10)]
print(l2)
l3 = [x ** 2 for x in range(10) if x % 2 == 0]
print(l3)
l4 = [(x+1,y+1) for x in range(2) for y in range(2)]
print(l4)
l5 = [x for x in range(1,101) if x % 5 ==0]
print(l5)
a = sum(x for x in range(10)) # 生成器表达式
print(a)
