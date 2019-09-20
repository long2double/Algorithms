"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [1],
  [1,2],
  [1,2,3],
  [2],
  [2,3],
  [3],
]
"""


class Solution:
    def subsets(self, nums):
        res = []
        if nums == []:
            return res

        for i in range(len(nums)):
            sub = []
            self.find_sub_sets(i, nums, sub, res)
        return res

    def find_sub_sets(self, i, nums, sub, res):
        if i >= len(nums):
            return
        sub.append(nums[i])
        res.append(sub[:])
        self.find_sub_sets(i + 1, nums, sub, res)


if __name__ == '__main__':
    S = Solution()
    arr = [1, 2, 3, 4]
    print(S.subsets(arr))

