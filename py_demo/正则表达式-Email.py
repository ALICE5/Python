#正则表达式
# -*- coding: utf-8 -*-
import re

#版本一可以验证出类似的Email
# test = input('please enter:')
# re_mode = re.compile(r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,4})$')
# if re_mode.match(test):
# 	print('ok')
# else:
# 	print('failed')


#版本二可以验证并提取出带名字的Email地址

Email=input('please enter the Email:')
re_mode=re.compile(r'<([a-zA-Z]*\s+[a-zA-Z]*)>\s+[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
we = re_mode.match(Email)
if we:
	print('This is %s' % we.groups())
else:
	print('failed!')
