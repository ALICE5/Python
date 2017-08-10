# 敏感词文本文件 filtered_words.txt 当用户输入敏感词语则用 星号 * 替换
# 例如当用户输入「北京是个好城市」 则变成「**是个好城市」

# -*-coding:utf-8-*-
import string


class senseWord():
    def __init__(self):
        self.list = []
        self.word = []
        inputfile = file('filtered_word.txt', 'r')
        for lines in inputfile.readlines():
            self.list.append(lines.decode('utf-8').encode('gbk'))  # I've set the file coding type as utf-8
        inputfile.close()
        self.list = map(string.strip, self.list);

    def checkWord(self, word):
        flag = False
        for words in self.list:
            if words in word:
                self.word.append(words)
                flag = True
        return flag

    def getWord(self):

        return self.word

# 测试
if __name__ == '__main__':
    myCheck = senseWord()
    while True:
        ipstr = str(raw_input())
        if ipstr:
            if (myCheck.checkWord(ipstr)):
                senseList = myCheck.getWord()
                for items in senseList:
                    length = len(items.decode('gbk'))
                    torep = '*';
                    for i in range(1, length):
                        torep += '*'
                    ipstr = ipstr.replace(items, torep)
                print
                ipstr
            else:
                print
                ipstr
        else:
            break