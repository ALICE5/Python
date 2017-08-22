'''
request 用来网页抓取
beautifulsoup和正则表达式 用来网页内容解析

'''

import requests
import re
from bs4 import BeautifulSoup
sum = 0
r = requests.get('https://book.douban.com/subject/1084336/comments/')
soup = BeautifulSoup(r.text,'html.parser')
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s,r.text)
for star in p:
    sum += int(star)
print(sum)
print(p)

