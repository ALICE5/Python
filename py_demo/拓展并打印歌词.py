# -*- coding: utf-8 -*-
'''

(1) 创建一个文件Blowing in the wind.txt

(2) 在文件头部插入歌名“Blowin’ in the wind”

(3) 在歌名后插入歌手名“Bob Dylan”

(4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.”

(5) 在屏幕上打印文件内容

'''

def insert_line(lines): # 传入列表
    lines.insert(0,"Blowin’ in the wind\n\n")
    lines.insert(1,"Bob Dylan\n\n")
    lines.append('\n\n1962 by Warner Bros. Inc.')
    return ''.join(lines) # 返回字符串


with open('Blowing in the wind.txt','r+') as f:
    lines = f.readlines()
    print(lines)
    string = insert_line(lines)
    print(string)
    f.seek(0) # 将指针指到开始 否则写入为空 因为是从指针所指到地方往后写入文件
    # seek() 方法用于移动文件读取指针到指定位置
    f.write(string)