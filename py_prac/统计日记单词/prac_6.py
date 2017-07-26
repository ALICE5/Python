# 有一个目录放了多篇日记 都是 txt 文件 为了避免分词的问题假设内容都是英文 请统计出你认为每篇日记最重要的词

import os
import re

# re.compile(pattern[, flags]) 把一个正则表达式pattern编译成正则对象 以便可以用正则对象的match和search方法
# os.path.splitext() 分解文件名的扩展名

def findWord(DirPath):
    if not os.path.isdir(DirPath):
        # os.path.isdir()函数判断某一路径是否为目录
        return
    fileList = os.listdir(DirPath)
    reObj = re.compile('\b?(\w+)\b?')
    # 由于正则表达式要反复使用所以使用 预编译
    # '?'表示匹配前一个字符重复0次到1次 '+'表示匹配前一个字符重复1次到无限次
    # \w -> [a-zA-Z0-9_]
    for file in fileList:
        filePath = os.path.join(DirPath, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.txt':
        # 若filePath是文件且后缀为 .txt 则执行如下
            with open(filePath) as f:
                data = f.read()
                words = reObj.findall(data)
                # findall(string) 以列表的形式返回能匹配的子串
                wordDict = dict()
                for word in words:
                    word = word.lower()
                    if word in ['a','the','to','i','in','you']:
                        continue
                    if word in wordDict:
                        wordDict[word] += 1
                    else:
                        wordDict[word] = 1
            wordList = sorted(wordDict.items(),key=lambda t: t[1],reverse=True)
            # 参数key为关键词 上面的意思是按元组里的第二个元素进行排序 reverse则进行降序排列
            print('file: %s->the most word: %s' % (file,wordList[0]))

if __name__ == '__main__':
    findWord('./text')