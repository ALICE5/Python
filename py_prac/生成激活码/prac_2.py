# 用 Python 生成随机的邀请码
# https://liam0205.me/2015/05/07/generator-of-invitation-code-in-python/

import random,string

# 产生15位随机串 包含数字和大小写字母
# ascii_letters是生成所有字母从a-z和A-Z digits是生成所有数字0-9
# choice(sequence)可以在一个有序的类型中（list、tuple 或 string）随机选取一个元素
poolOfChar = string.ascii_letters + string.digits
random_codes = lambda x,y : ''.join([random.choice(x) for i in range(y)])

print(random_codes(poolOfChar,15))

# 填充空位
# 主键通常是一个递增的整数序列 若主键值从1增加到1000 那么主键的位数就会从1增加到4
# 对于邀请码来说需要固定其长度 反应到主键上需要固定主键的长度
# 最简单的办法就是用 0 填充（pad）空位
class LengthError(ValueError):
    def __init__(self,arg):
        self.args = arg

def pad_zero_to_left(inputNumString, totalLength):
    lengthOfInput = len(inputNumString)
    if lengthOfInput > totalLength:
        raise LengthError("The length of input is greater than the total length.")
    else:
        return '0' * (totalLength - lengthOfInput) + inputNumString

# 拼接
