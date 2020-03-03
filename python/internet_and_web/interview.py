#!/usr/bin/python
# -*- coding: utf-8 -*-
import pdb


# def getMax(listGroup): # 获取人数最多的项目组
#     maxValueKey = ''
#     maxValue = 0
#     for key, value in listGroup.items():
#         if value > maxValue:
#             maxValue = value
#             maxValueKey = key
#     return maxValueKey
#
#
# def change(listGroup, maxValueKey): # 对各项目组进行一次优化
#     for groupName, groupNum in listGroup.items():
#         if groupName == maxValueKey:
#             listGroup[groupName] -= 3
#         else:
#             listGroup[groupName] += 1
#
#
# if __name__ == '__main__':
#     listGroup = {'groupA': 10, 'groupB': 7, 'groupC': 5, 'groupD': 4} # 初始化
#     for i in range(120): # 120是十年共优化120次
#         maxValueKey = getMax(listGroup)
#         change(listGroup, maxValueKey)
#     print(listGroup)


# 邀请码检测

# def getSum(numList, isEven=False):  # 自定义数组元素求和
#     keyToValueMap = {  # 建值对应情况
#         'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5,
#         'o': 6, 'p': 7, 'r': 8, 's': 9, 't': 1, 'u': 2, 'v': 3, 'w': 4, 'x': 5, 'y': 6, 'z': 7, '1': 1, '2': 2, '3': 3,
#         '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
#     }
#     sumValue = 0
#     if not isEven:  # 奇数的求和方式
#         for num in numList:
#             value = keyToValueMap.get(num)
#             sumValue += value
#     else:  # 偶数求和方式
#         for num in numList:
#             value = keyToValueMap.get(num) * 2
#             if value > 10:
#                 value -= 9
#             sumValue += value
#     return sumValue
#
#
# def isInvitationCode(code):
#     if len(code) != 16:
#         return 'error'
#     code = code[::-1]  # 数组反转
#     oddList = code[0::2]  # 取奇数位元素
#     evenList = code[1::2]  # 取偶数位元素
#     oddSum = getSum(oddList)
#     evenSum = getSum(evenList, isEven=True)
#     if (evenSum + oddSum) % 10 != 0:
#         return 'error'
#     return 'ok'
#
#
# if __name__ == '__main__':
#     code = '123456789abcdefd'
#     print(isInvitationCode(code))


# 游戏币问题
#动态规划

# listRes = []
# # 有趣的两位数
# for i in range(10, 101):
#     for j in range(10, 101):
#         if i * j == int(str(i)[::-1]) * int(str(j)[::-1]):
#            listRes.append((i, j))
# print(listRes)



# val = [1,5,10,20,50,100]
# n = int(input())
# def solution(n):
#     if n  == 0:
#         return 0
#     a = [1 for i in range(n+1)]
#     for i in range(1,6):
#         for j in range(i,n+1):
#             if j >= val[i]:
#                 a[j] += a[j - val[i]]
#     return a[n]
# # print a
# print(solution(n))
