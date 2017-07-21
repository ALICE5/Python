# coding=utf-8
import re
import requests #requests用于网络请求
import pdfkit
from bs4 import BeautifulSoup #beautifulsoup用于操作html数据

#step 1: 用requests把整个页面加载到本地 再用beautifulsoup操作提取内容
#用 soup.find_all 函数找到正文标签 然后把正文部分的保存到a.html文件
def parse_url_to_html(url,f_name):
    response = requests.get(url)
    soup =  BeautifulSoup(response.content,"html.parser")
    body = soup.find_all(class_="x-wiki-content")[0]

    title = soup.find('h4').get_text()
    center_tag = soup.new_tag("center")
    title_tag = soup.new_tag('h1')
    title_tag.string = title
    center_tag.insert(1, title_tag)
    body.insert(1, center_tag)
    # font_tag = soup.new_tag('20px')
    # body.insert(1,font_tag)

    html=str(body)
    # pattern = "(<img .*?src=\")(.*?)(\")"   # body中的img标签的src相对路径的改成绝对路径
    #
    # def func(m):
    #     if not m.group(2).startswith("http"):
    #         rtn = "".join([m.group(1), self.domain, m.group(2), m.group(3)])
    #         return rtn
    #     else:
    #         return "".join([m.group(1), m.group(2), m.group(3)])
    #
    # html = re.compile(pattern).sub(func, html)
    # html = html_template.format(content=html)
    html = html.encode("utf-8")


    with open (f_name,'wb') as f:   #with语句自动调用close()
        f.write(html)


#step 2: 获取所有url目录列表 把页面左侧所有url解析出来
def get_url_list():
    response = requests.get("https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content,"html.parser")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    #页面上有两个uk-nav uk-nav-side属性 真正要取的目录列表是第一个
    urls = []
    for li in menu_tag.find_all("li"):
        url = "https://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls

#step 3: 把html转换成pdf文件 只需要调用pdfkit.from_file
def save_pdf(htmls):
    options = {
        'page-size':'A5',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding':"utf-8",
        'custom-header':[
            ('Accept-Ecoding','gzip')
        ],
        'outline-depth': 10,
    }
    pdfkit.from_file(htmls,"py.pdf",options=options)


if __name__=='__main__':

    htmls=[]
    for index,url in enumerate(get_url_list()):
        f_name = ".".join([str(index), "html"])
        html = parse_url_to_html(url,f_name)
        htmls.append(f_name)
    save_pdf(htmls)