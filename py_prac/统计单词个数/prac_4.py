# 任一个英文的纯文本文件 统计其中的单词出现的个数
# w/r/wt/rt都是python里面文件操作的模式 w是写模式 r是读模式
# rt模式下 python在读取文本时会自动把\r\n转换成\n
# wt模式下 python写文件时会用\r\n来表示换行
# 但只在Windows模式下使用：windows用的是\r\n两个ASCII字符来表示换行

# -*-coding:utf-8-*-

import os
import re

def word_statistics(filePath):
    wordDict = {}
    with open(filePath,'r') as f:
        for line in f:
            words = re.split('[,."\-\s]\s*',line)
          #or words = re.split('[,."\-\s]+',line)
            for word in words:
                if word.lower() in wordDict and word.isalpha():
                #Python isalpha() 方法检测字符串是否只由字母组成
                    wordDict[word.lower()]+= 1
                elif word.lower() not in wordDict and word.isalpha():
                    wordDict[word.lower()] = 1

    wordStored = sorted(zip(wordDict.keys(),wordDict.values()))

    for word,count in wordStored:
        print(word,':',count)

if __name__ == '__main__':
    word_statistics(r'abc.txt')