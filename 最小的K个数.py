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
