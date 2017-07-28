# 一个HTML文件 找出里面的链接

#! /usr/bin/env/ python3
# -*- coding: utf-8 -*-

__author__ = 'Alice'

import urllib.request
from bs4 import BeautifulSoup

url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page,'html.parser')
links = soup.find_all('a')
# links = soup.select('a')

for link in links:
    print(link['href'])
    # print(link)

