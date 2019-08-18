"""
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if k > length or k == 0:
            return []
        res = []
        for i in range(length):
            min = i
            for j in range(i + 1, length):
                if tinput[j] < tinput[min]:
                    min = j
            tinput[i], tinput[min] = tinput[min], tinput[i]
            res.append(tinput[i])
            if len(res) == k:
                return res
