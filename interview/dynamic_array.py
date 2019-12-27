#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


class Dynamic_array(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dataList = [None] * self.capacity
        self.size = 0

    def pushBack(self, value):
        '''向列表末尾追加value'''
        if self.size == self.capacity:
            # 扩展空间
            self.dataList = self.dataList + [None] * self.capacity
            self.capacity = self.capacity * 2
        self.dataList[self.size] = value
        self.size += 1

    def removeByPos(self, pos):
        '''移除某个位置的元素'''
        if pos < 0 or pos >= self.size:
            return
        for i in range(pos, self.size):
            self.dataList[i] = self.dataList[i + 1]
        self.size -= 1

    def removeByValue(self, value):
        '''移除某个值为value的元素'''
        pos = self.findByValue(value)
        self.removeByPos(pos)

    def findByValue(self, value):
        '''获取某个value的索引值'''
        pos = -1
        for i in range(self.size):
            if self.dataList[i] == value:
                pos = i
        return pos

    def findByPos(self, pos):
        '''获取某个索引位置的值'''
        if pos < 0 or pos >= self.size:
            return
        return self.dataList[pos]

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity

    def __str__(self):
        dataList = [data for data in self.dataList if data != None]
        resultMap = {
            'dataList': dataList,
            'size': self.size,
            'capacity': self.capacity
        }
        return json.dumps(resultMap)


if __name__ == '__main__':
    # 初始化测试
    myarr = Dynamic_array(20)
    print(myarr)

    # 追加测试
    for i in range(10):
        myarr.pushBack(i)
    print(myarr)

    # 删除测试
    myarr.removeByPos(1)
    myarr.removeByValue(5)
    myarr.removeByValue(9)
    print(myarr)

    # 查找测试
    print(myarr.findByValue(5))
    print(myarr.findByPos(5))


