# -*-coding:utf-8 -*-
from path import *
import os

class SimilarWordUtils:

    def __init__(self):

        with open(SIMILAR_WORD_FILE,'r') as f:
            od = f.readlines()

        self.data = []
        for d in od:
            if d[7] == '=':
                # 只取近义词
                d = d.split(' ')[1:]
                if len(d) > 0:
                    d[-1] = d[-1][:-1]
                self.data.append(d)
            
        self.book = dict()
        for i in range(len(self.data)):
            for word in self.data[i]:
                self.book[word] = i

    def getSimilarWord(self,word):
        result = []
        try:
            result = self.data[self.book[word]]
        except:
            return result
        else:
            return result

if __name__ == '__main__':

    import io
    import sys
    #改变标准输出的默认编码
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

    similar_tools = SimilarWordUtils()
    print(similar_tools.getSimilarWord("我"))
    print(similar_tools.getSimilarWord("你"))
    print(similar_tools.getSimilarWord("他"))
    print(similar_tools.getSimilarWord("自行车"))
    print(similar_tools.getSimilarWord("是的"))
