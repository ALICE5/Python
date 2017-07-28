# 一个HTML文件 找出里面的正文

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Alice'

import urllib.request  # urllib.request urllib.error
from bs4 import BeautifulSoup

url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
page = urllib.request.urlopen(url)
# print(page.read())
# urllib.urlopen(url[, data[, proxies]])
# 创建一个表示远程url的类文件对象 然后像本地文件一样操作这个类文件对象来获取远程数据

# soup = BeautifulSoup(page,'html.parser')
# print(soup.title)
# print(soup.body)
# 以上是简单提取title和body

page.coding = 'utf-8'

soup = BeautifulSoup(page,'html.parser')
# article = soup.select('div.x-wiki-content.x-main-content')
article = soup.select('div.x-wiki-content.x-main-content')[0].get_text()

print(article)
