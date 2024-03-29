"""
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续
的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很
快的找出所有和为S的连续正数序列? Good Luck!
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum == 1:
            return []
        array = []
        for i in range(1, tsum):
            array.append(i)

        start = 0
        end = 1
        res = []
        while start < end:
            if sum(array[start:end]) < tsum:
                end += 1
            elif sum(array[start:end]) > tsum:
                start += 1
            else:
                res.append(array[start: end])
                end += 1
                start += 1
            if end > tsum // 2 + 1:
                break
        return res
