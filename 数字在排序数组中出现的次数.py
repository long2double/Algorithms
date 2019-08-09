"""
题目描述
统计一个数字在排序数组中出现的次数。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # 先找到最左侧的
        begin = 0
        end = len(data) - 1
        first = None
        while begin <= end:
            mid = (begin + end) // 2
            if data[mid] < k:
                begin = mid + 1
            elif data[mid] > k:
                end = mid - 1
            elif begin == mid or data[mid - 1] != k:
                first = mid
                break
            else:
                end -= 1

        # 在找到最右侧的
        begin = 0
        end = len(data) - 1
        second = None
        while begin <= end:
            mid = (begin + end) // 2
            if data[mid] < k:
                begin = mid + 1
            elif data[mid] > k:
                end = mid - 1
            elif mid == end or data[mid + 1] != k:
                second = mid
                break
            else:
                begin += 1

        # 个数等于左侧-右侧+1
        if first is None:
            return 0
        else:
            return second - first + 1
