#!/usr/bin/python
# -*- coding: utf-8 -*-

def getN(n):
    if n < 2:
        return 1
    return getN(n-1) + getN(n-2)


print(getN(10))



# 求两个字符串的第二长公共单词
def getSecondWord(str1, str2):
    substrList = []
    str1List = str1.split(' ')
    str2List = str2.split(' ')
    for word in str1List:
        if word in str2List:
            substrList.append(word)
    resultList = sorted(substrList, key=lambda x:len(x), reverse=True)
    return resultList[1]




if __name__ == '__main__':
    str1 = 'This is C programming text'
    str2 = 'This is a text for C programming'
    print(getSecondWord(str1, str2))

