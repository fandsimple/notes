#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

MAX_SIZE = 50


class StackArray(object):
    dataList = None
    size = None

    def __init__(self):
        self.dataList = [None] * 50
        self.size = 0

    def push(self, value):
        '''入栈'''
        if self.size == MAX_SIZE:
            return
        if value == None:
            return
        self.dataList[self.size] = value
        self.size += 1

    def pop(self):
        '''出栈'''
        if self.size == 0:
            return
        popItem = self.dataList[self.size - 1]
        self.dataList[self.size - 1] = None
        self.size -= 1
        return popItem

    def getPopValue(self):
        '''查看栈顶元素'''
        if self.size == 0:
            return
        return self.dataList[self.size - 1]

    def getSize(self):
        '''查看当前入栈元素个数'''
        return self.size

    def clearStack(self):
        '''清空栈'''
        for i in range(self.size):
            self.dataList[i] = None
        self.size = 0

    def __str__(self):
        '''打印'''
        result = {
            'dataList': self.dataList,
            'size': self.size
        }
        return json.dumps(result)



if __name__ == '__main__':
    myStack = StackArray()
    print(myStack)

    for i in range(10):
        myStack.push(i)
    print(myStack)

    print(myStack.pop())
    print(myStack)

    myStack.clearStack()
    print(myStack)