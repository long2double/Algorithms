"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        # 从两边向中间移动
        begin = 0
        end = len(array) - 1

        while begin < end:
            sums = array[begin] + array[end]
            if sums > tsum:
                end -= 1
            elif sums < tsum:
                begin += 1
            else:
                return [array[begin], array[end]]
        return []

        # 哈希
        # for i in array:
        #     j = tsum - i
        #     if j in array:
        #         return [i, j]
        # return []