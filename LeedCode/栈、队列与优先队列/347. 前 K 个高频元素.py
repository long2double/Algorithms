"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]
"""


class Solution:
    def topKFrequent(self, nums, k):
        has_map = {}
        for i in nums:
            if i not in has_map:
                has_map[i] = 1
            else:
                has_map[i] += 1

        dict_ = sorted(has_map.items(), key=lambda d: d[1], reverse=True)
        res = []
        i = 0
        for key, value in dict_:
            res.append(key)
            i += 1
            if i == k:
                break
        return res

