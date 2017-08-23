# 字符串格式化输出
aStr = "Hello, World!"
bStr = aStr[:7] + "Python!?"
count = 0
for ch in bStr:
    if ch in ',.!?"':
        count += 1
print('There are %d punctuation marks.' % count)
print('There are {0:d} punctuation marks.'.format(count)) # {参数序号:参数类型}

age, height = 21, 1.758
print("Age:{0:<5d}, Height:{1:5.2f}".format(age,height))

cCode = ['AXP','BA','CAT','CSCO','CVX']
cPrice = ['78.51','184.76','96.39','33.71','106.09']
for i in range(5):
    print('{0:<8d}{1:8s}{2:8s}'.format(i,cCode[i],cPrice[i]))
print('I get {:d}{{}}!'.format(32))

# 判断回文串的3个方法
sStr = 'acdhdca'
if(sStr == ''.join(reversed(sStr))):
    print('Yes')
else:
    print('No')

import operator
sStr = 'acdhdca'
if operator.eq(sStr,''.join(reversed(sStr)))==1:
    print('Yes')
else:
    print('No')

sStr = 'acdhdca'
if sStr == sStr[::-1]:
    print('Yes')
else:
    print('No')

# 字符串函数
song = "Blowing in the wind"
print(song.find("the"))
print(song.find("the",8,12))
print(song.lower())
print(song.split(' '))
print(song.replace("the","that"))
print(song)

aList = ["hello","world"]
print(' '.join(aList))
y = "你好"
z = y.encode('utf-8')
print(z)
t = z.decode()
print(t)
print((b'\xe6\x89\x8e\xe5\xbf\x83\xe4\xba\x86\xef\xbc\x8c\xe8\x80\x81\xe9\x93\x81').decode())

# 判断双引号的内容是否满足标题格式 满足与否均输出
aStr = 'What do you think of this saying "Np pain, No gain"?'
lindex = aStr.index('\"',0,len(aStr))
rindex = aStr.rindex('\"',0,len(aStr)) # 返回子字符串在字符串中最后出现的位置
tempStr = aStr[lindex+1 : rindex]
# tempStr = aStr.split("\"")[1]
if tempStr.istitle():
    print('It is title format.')
else:
    print('It is not title format.')
print(tempStr.title())
print('\x65')