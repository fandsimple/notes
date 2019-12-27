#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy

'''    
O(1)常数阶 < O(logn)对数阶 < O(n)线性阶 < O(n2)平方阶 < O(n3)(立方阶) < O(2n) (指数阶)
'''


class FandsimpleSort(object):
    @staticmethod
    def bubble_sort(dataList):  # 冒泡排序
        '''
        时间复杂度：o(n*2)
        空间复杂度：o(1)
        稳定性：稳定
        '''
        for i in range(len(dataList) - 1):
            for j in range(len(dataList) - 1 - i):
                if dataList[j] > dataList[j + 1]:
                    dataList[j], dataList[j + 1] = dataList[j + 1], dataList[j]
        return dataList

    @staticmethod
    def select_sort(dataList):  # 选择排序
        '''
        时间复杂度：o(n*2)
        空间复杂度：o(1)
        稳定性：不稳定
        '''
        for i in range(len(dataList) - 1):
            minIndex = i
            for j in range(i + 1, len(dataList)):
                if dataList[minIndex] > dataList[j]:
                    minIndex = j
            dataList[i], dataList[minIndex] = dataList[minIndex], dataList[i]
        return dataList

    @staticmethod
    def insert_sort(dataList):  # 插入排序
        '''
        时间复杂度：o(n*2)
        空间复杂度：o(1)
        稳定性：不稳定
        '''
        for i in range(1, len(dataList)):
            if dataList[i] < dataList[i - 1]:
                tem = dataList[i]
                j = i - 1
                while j >= 0 and dataList[j] > tem:
                    dataList[j + 1] = dataList[j]
                    j -= 1
                dataList[j + 1] = tem
        return dataList

    @staticmethod
    def inser_plus_sort(dataList):  # 希尔排序
        '''
        时间复杂度：o(n*2)
        空间复杂度：o(1)
        稳定性：不稳定
        '''
        pass

    @classmethod
    def quick_sort(cls, dataList):  # 快排（内存耗费大）
        '''
        时间复杂度：o(nlogn)
        空间复杂度：o(logn)
        稳定性：不稳定
        '''

        if len(dataList) < 2:
            return dataList
        tem = dataList.pop()
        less_data_list = [data for data in dataList if data < tem]
        big_data_list = [data for data in dataList if data >= tem]
        return cls.quick_sort(less_data_list) + [tem] + cls.quick_sort(big_data_list)

    @classmethod
    def quick_sort_stand(cls, array, left, right): # 快排（教材版）
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] <= key:
                left += 1
            array[right] = array[left]
        array[right] = key
        cls.quick_sort(array, low, left - 1)
        cls.quick_sort(array, left + 1, high)

    @classmethod
    def heapify(cls, arry, length, index): # 堆化函数
        if index >= length:
            return
        max = index
        lc_index = index * 2 + 1
        rc_index = index * 2 + 2
        if lc_index < length and arry[max] < arry[lc_index]:
            max = lc_index
        if rc_index < length and arry[max] < arry[rc_index]:
            max = rc_index
        if max != index:
            arry[index], arry[max] = arry[max], arry[index]
            cls.heapify(arry, length, max)
    @classmethod
    def build_heap(cls, arry, length): # 创建大顶堆
        startIndex = (length - 1)/2
        for i in range(startIndex, -1, -1):
            cls.heapify(arry, length, i)

    @ classmethod
    def heap_sort(cls, arry, length): # 堆排序
        cls.build_heap(arry, length)
        for i in range(length-1, 0, -1):
            arry[0], arry[i] = arry[i], arry[0]
            cls.heapify(arry, i, 0)


if __name__ == '__main__':
    dataList = [1, 5, 3, 2, 4, 6, 9, 8, 7]
    print(FandsimpleSort.bubble_sort(copy.deepcopy(dataList)))  # 冒泡
    print(FandsimpleSort.select_sort(copy.deepcopy(dataList)))  # 选择排序
    print(FandsimpleSort.quick_sort(copy.deepcopy(dataList)))  # 快排
    print(FandsimpleSort.insert_sort(copy.deepcopy(dataList)))  # 插入排序

    # 堆排序
    arry = [4, 10, 3, 5, 1, 2]
    FandsimpleSort.heap_sort(arry, 6)
    print(arry)


