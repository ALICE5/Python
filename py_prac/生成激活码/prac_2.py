# 用 Python 生成随机的邀请码
# https://liam0205.me/2015/05/07/generator-of-invitation-code-in-python/

import random,string

# 产生15位随机串 包含数字和大小写字母
# ascii_letters是生成所有字母从a-z和A-Z digits是生成所有数字0-9
# choice(sequence)可以在一个有序的类型中（list、tuple 或 string）随机选取一个元素
poolofChar = string.ascii_letters + string.digits
random_codes = lambda x,y : ''.join([random.choice(x) for i in range(y)])

print random_codes(poolofChar,15)

# 填充空位



# 拼接

