#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 汉诺塔 递归函数
def move(n,a,b,c):
	if n==1:
		print('move', a, 'to', c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)