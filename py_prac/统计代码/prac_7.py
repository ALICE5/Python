# 有个目录里面是写过的程序 统计一下共多少行代码 包括空行和注释 分别列出来

# -*-coding:utf-8-*-

import sys
import os
import re

def cal(path):
    filelist = os.listdir(path)
    # print filelist
    filelist = (item for item in filelist if item.endswith(('.py')))
    ret = [0,0,0]
    for item in filelist:
        res = calfile(path,item)
        for i in (0,1,2):
            ret[i] += res[i]
    return tuple(ret)

def calfile(path,filename):
    totLine = 0
    blankLine = 0
    commentLine = 0
    fileObj = open(path + filename,'r')
    lineList = fileObj.readlines()
    totLine = len(lineList)
    for line in lineList:
        pattern = re.compile(r'(\s*)#')
        pattern1 = re.compile(r'(\s*)$')
        if pattern.match(line):
            commentLine += 1
        if pattern1.match(line):
            blankLine += 1
    fileObj.close()
    return totLine,blankLine,commentLine

path = sys.argv[1]
data = cal(path)
dic = dict(zip(['total line','blank line','comment line'],list(data)))
print(dic)