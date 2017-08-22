# -*- coding:utf-8 -*-
"""
Crawler 

请在豆瓣任意找一本图书, 抓取它某一页的短评并进行页面解析将短评文字抽取后输出,
再对其中的评分进行抽取计算其总分.

@author: Alice

"""

import requests
from bs4 import BeautifulSoup
import re

sum = 0
r = requests.get('https://book.douban.com/subject/27026325/comments/')
soup = BeautifulSoup(r.text,'html.parser')
pattern = soup.find_all('p','comment-content')
for item in pattern:
    print(item.string+'\n')

pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s,r.text)
for star in p:
    sum += int(star)
print('total mark: ')
print(sum)

print(p)