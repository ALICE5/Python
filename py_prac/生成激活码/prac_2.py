# 用 Python 生成随机的邀请码
# https://liam0205.me/2015/05/07/generator-of-invitation-code-in-python/

import random,string

# 产生15位随机串 包含数字和大小写字母
# ascii_letters是生成所有字母从a-z和A-Z digits是生成所有数字0-9
# choice(sequence)可以在一个有序的类型中（list、tuple 或 string）随机选取一个元素
poolOfChar = string.ascii_letters + string.digits
random_codes = lambda x,y : ''.join([random.choice(x) for i in range(y)])
# ''.join(['1','2','3']) => '123'

# print(random_codes(poolOfChar,15))

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
# 得到了主键和随机序列产生的方法 剩下的问题就是要拼接起来
# 拼接完成之后 还要保证能够很容易地找到主键的部分
# 所以在主键和随机串之间加上一个固定的字母 比如A 作为标识符
# 整个邀请码子串最后一个A之后 就是主键部分
def invitation_code_generator(quantity, lengOfRandom, lenOfKey):
    placeHoldChar = "A"
    for index in range(quantity):
        tempString = ""
        try:
            yield random_codes(poolOfChar,lengOfRandom) + placeHoldChar + pad_zero_to_left(str(index),lenOfKey)
        except LengthError:
            print("Index exceeds the length of master key.")

# 生成200个邀请码

i = 1
for invitationCode in invitation_code_generator(200,15,4):
    print(str(i)+ ':' + invitationCode)
    i = i + 1
