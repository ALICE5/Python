'''

https://book.douban.com/robots.txt 
进入/robots.txt可以查看网站的爬虫协议

'''

import requests
r = requests.get('https://book.douban.com/subject/1084336/comments/')
# print(r.status_code)
# 状态码若为200 则为正常
# print(r.text)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')
pattern = soup.find_all('p','comment-content')
for item in pattern:
    print(item.string)



# from bs4 import BeautifulSoup
# markup = '<p class="title"><b>The Little Prince</b></p>'
# soup = BeautifulSoup(markup,"xml")
# print(soup.b)
# print(type(soup.b))
# tag = soup.p
# print(tag.name,' ',tag.attrs)
# print(tag['class'],' ',tag.string,' ',type(tag.string))
# fa = soup.find_all('b')
# print(fa)


# import requests
# re = requests.get('http://money.cnn.com/data/dow30/')
# print(re.text)
# # text自动推测文本编码并进行解码
# # re.content re.encoding='utf-8' re.json()

