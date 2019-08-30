"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        res = []
        if nums == []:
            return []
        nums.sort()

        length = len(nums)
        for a in range(length - 2):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            new_tar = 0 - nums[a]
            b, c = a + 1, length - 1
            while b < c:
                if nums[b] + nums[c] == new_tar:
                    res.append([nums[a], nums[b], nums[c]])
                    while b < c and nums[b] == nums[b + 1]:
                        b += 1
                    while b < c and nums[c] == nums[c - 1]:
                        c -= 1
                    b += 1
                    c -= 1
                elif nums[b] + nums[c] < new_tar:
                    b += 1
                else:
                    c -= 1
        return res
