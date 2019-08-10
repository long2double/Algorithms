"""
题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶
数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数
据的中位数。
"""

# 利用堆，有待改进
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []

    def Insert(self, num):
        # write code here
        self.res.append(num)

    def GetMedian(self):
        # write code here
        res = sorted(self.res)
        length = len(res) // 2

        if len(res) % 2 == 0:

            return (res[length - 1] + res[length]) / 2
        else:
            return res[length]