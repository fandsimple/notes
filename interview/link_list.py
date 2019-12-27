#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pdb


# 节点定义
class Node(object):
    data = None
    nextNode = None


# 链表定义
class LinkList(object):
    head = None
    size = None

    def __init__(self):
        self.head = Node()
        self.head.data = None
        self.head.nextNode = None
        self.size = 0

    def insertByPos(self, pos, value):
        '''指定位置插入'''
        if pos < 0 or pos > self.size:
            return
        newNode = Node()
        newNode.data = value
        newNode.nextNode = None
        currentNode = self.head
        if pos == 0:
            newNode.nextNode = self.head.nextNode
            self.head.nextNode = newNode
        else:
            for i in range(pos):
                currentNode = currentNode.nextNode
            newNode.nextNode = currentNode.nextNode
            currentNode.nextNode = newNode
        self.size += 1

    def delByPos(self, pos):
        '''删除指定位置的值'''
        if pos < 0 or pos >= self.size:
            return
        currentNode = self.head
        if pos != 0:
            for i in range(pos):
                currentNode = currentNode.nextNode
        delNode = currentNode.nextNode
        currentNode.nextNode = delNode.nextNode
        del delNode
        self.size -= 1

    def getSize(self):
        '''获得链表的长度'''
        return self.size

    def findByValue(self, value):
        '''查找value在链表中的位置'''
        currentNode = self.head.nextNode
        pos = 0
        while currentNode:
            if currentNode.data == value:
                break
            pos += 1
            currentNode = currentNode.nextNode
        if pos == self.size:
            pos = -1
        return pos

    def getFisrtNode(self):
        '''获取第一个节点'''
        currentNode = self.head.nextNode
        return currentNode

    def __str__(self):
        dataList = []
        currentNode = self.head.nextNode
        while currentNode:
            dataList.append(currentNode.data)
            currentNode = currentNode.nextNode
        resultData = {
            'dataList': dataList,
            'size': self.size,
        }
        return json.dumps(resultData)


if __name__ == '__main__':
    # 创建单链表
    linkList = LinkList()
    print(linkList)

    # 插入数据
    for i in range(10):
        linkList.insertByPos(i, str(i))
    print(linkList)

    # 测试删除数据
    linkList.delByPos(9)
    linkList.delByPos(0)
    print(linkList)

    # 测试获取列表长度
    print(linkList.getSize())

    # 测试查找数据
    print(linkList.findByValue("1"))


