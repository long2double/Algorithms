"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_diff = 2 ** 32
        min_value = 2 ** 32

        length = len(nums)
        for a in range(length - 2):
            b, c = a + 1, length - 1
            while b < c:
                sums = nums[a] + nums[b] + nums[c]
                if abs(target - sums) < min_diff:
                    min_diff = abs(target - sums)
                    min_value = sums

                if sums < target:
                    b += 1
                elif sums > target:
                    c -= 1
                else:
                    return target
        return min_value

