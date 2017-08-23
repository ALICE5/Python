# -*- coding: utf-8 -*-
'''

定义函数countchar()按字母表顺序统计字符串中26个字母出现的次数（不区分大小写）。
例如字符串“Hope is a good thing.”的统计结果为：

[1, 0, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 3, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]

'''

def countChar(s):
    lst = [0] * 26
    for i in range(len(s)):
        if s[i] >= 'a' and s[i]<= 'z':
            lst[ord(s[i])-ord('a')] += 1
    print(lst)

if __name__ == '__main__':
    s = 'Hope is a good thing.'
    s = s.lower()
    countChar(s)