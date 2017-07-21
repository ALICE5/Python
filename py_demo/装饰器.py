#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(anyValue):
	# 含参数情况
	if isinstance(anyValue, str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args):
				print("Begin Call: %s %s" % (anyValue,func.__name__))
				func()
				print("End Call.")
			return wrapper
		return decorator
	# 无参数情况
	else:
		@functools.wraps(anyValue)
		def wrapper(*args):
			print("Begin Call: %s " % anyValue.__name__)
			anyValue()	
			print("End Call.")
		return wrapper

# 无参数装饰器 解析过程
# 1.解释器发现@log，调用对应的log函数
# 2.log函数调用前指定了一个参数，传入的是@log下面修饰的函数，也就是f()
# 3.log执行 调用f()
@log
def f():
	print("Running Process")
f()

# 有参数装饰器 解析过程
# 1.
@log('execute')
def f1():
	print("Running Advanced Process")
f1()

