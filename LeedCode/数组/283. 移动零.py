"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        时间复杂度O(n)
        空间复杂度O(1)
        """
        #         length = len(nums)

        #         k = 0
        #         for i in range(length):
        #             if nums[i] != 0:
        #                 nums[k] = nums[i]
        #                 k += 1

        #         for j in range(k, length):
        #             nums[j] = 0
        #         return nums

        length = len(nums)
        k = 0
        for i in range(length):
            if nums[i] != 0:
                if i != k:  # 全为非0元素的情况，避免与自己交换
                    nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return nums



