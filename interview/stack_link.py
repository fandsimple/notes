#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


class Node(object):
    data = None
    nextData = None

class StackLink(object):
    size = None
    head = None

    def __init__(self):
        self.size = 0
        headNode = Node()
        self.head = headNode


    def push(self, value):
        '''入栈'''
        if value == None:
            return
        newNode = Node()
        newNode.data = value
        newNode.nextData = self.head.nextData
        self.head.nextData = newNode
        self.size += 1

    def pop(self):
        '''出栈'''
        if self.size == 0:
            return
        popNode = self.head.nextData
        self.head.nextData = popNode.nextData
        self.size -= 1
        del popNode

    def getPopValue(self):
        '''获得栈顶元素'''
        if self.size == 0:
            return
        return self.head.nextData.data

    def clearStack(self):
        '''清空栈'''
        if self.size == 0:
            return
        delNode = self.head.nextData
        del delNode
        self.head.nextData = None
        self.size = 0

    def getSize(self):
        '''获得入栈元素个数'''
        return self.size


    def __str__(self):
        '''打印'''
        dataList = []
        currentNode = self.head.nextData
        while currentNode:
            dataList.append(currentNode.data)
            currentNode = currentNode.nextData
        result = {
            'dataList': dataList,
            'size': self.size
        }
        return json.dumps(result)


if __name__ == '__main__':
    stackLink = StackLink()
    print(stackLink)

    for i in range(10):
        stackLink.push(i)
    print(stackLink)

    stackLink.pop()
    print(stackLink)

    print(stackLink.getPopValue())

    stackLink.clearStack()
    print(stackLink)