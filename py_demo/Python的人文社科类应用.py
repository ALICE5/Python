# from nltk.corpus import gutenberg
# allwords = gutenberg.words('shakespeare-hamlet.txt') # 单词+标点
# # print(len(allwords))
# # print(len(set(allwords)))
# # print(allwords.count('Hamlet'))
# # A = set(allwords)
# # longwords = [w for w in A if len(w)>12]
# # print(len(longwords))
# # print(sorted(longwords))
#
# from nltk.probability import *
# fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()]) # 所有单词对小写
# print(fd2.B()) # 不同单词的个数
# print(fd2.N()) # 所有单词的个数
# fd2.tabulate(20) # 取前20个数据
# fd2.plot(20)
# fd2.plot(20,cumulative=True)

from nltk.corpus import inaugural
from nltk.probability import *
fd3 = FreqDist([s for s in inaugural.words()])
print(fd3.freq('freedom'))
# 条件频率统计函数
cfd = ConditionalFreqDist(
    (fileid,len(w))
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    if fileid>'1980' and fileid<'2010'
)
print(cfd.items())
cfd.plot()