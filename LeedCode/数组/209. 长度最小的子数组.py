"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        length = len(nums)
        start, end = 0, -1
        sums = 0
        minSubLen = 2 ** 32
        while start < length:
            if sums < s:
                if end < length - 1:
                    end += 1
                    sums += nums[end]
                else:
                    if minSubLen == 2 ** 32:
                        return 0
                    else:
                        return minSubLen
            else:
                minSubLen = min(minSubLen, end - start + 1)
                sums -= nums[start]
                start += 1
        if minSubLen == 2 ** 32:
            return 0
        else:
            return minSubLen
