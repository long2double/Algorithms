"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsWithDup(self, nums):
        sub = []
        res = [[]]

        if nums == []:
            return res

        nums.sort()
        self.find_sub_set(0, nums, sub, res)
        result = list(set([tuple(i) for i in res]))  # 去重
        return result

    def find_sub_set(self, i, nums, sub, res):
        if i >= len(nums):
            return

        sub.append(nums[i])
        res.append(sub[:])
        self.find_sub_set(i + 1, nums, sub, res)
        sub.pop()
        self.find_sub_set(i + 1, nums, sub, res)
