# 处理敏感词文本文件 filtered_words.txt
# 当用户输入敏感词语 打印出 Freedom 否则打印出 Human Rights

# -*- coding:utf-8 -*-

def trans_to_word():
    word_filter = set()
    # set 是一组key的集合 重复元素在set中自动被过滤
    # add(key) 添加元素到set中 对于重复的元素没有效果 remove(key) 删除元素
    with open('filtered_words.txt') as f:
        for word in f.readlines():
            word_filter.add(word.strip())
    while True:
        s = input()
        if s == 'exit':
            break
        if s in word_filter:
            print('Freedom')
        else:
            print('Human Rights')

if __name__ == '__main__':
    trans_to_word()