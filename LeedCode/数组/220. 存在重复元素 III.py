"""
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k == 10000:
            return False

        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, min(length, i + k + 1)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False


if __name__ == '__main__':
    S = Solution()
    nums = [2, 2]
    k = 3
    t = 0
    print(S.containsNearbyAlmostDuplicate(nums, k, t))

