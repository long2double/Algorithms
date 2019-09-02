"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        has_map = {}
        for index, value in enumerate(nums):
            if value in has_map:
                if index - has_map[value] <= k:
                    return True
            # 不管在不在都需要更新哈希的索引值
            has_map[value] = index
        return False


if __name__ == '__main__':
    S = Solution()
    num = [1,2,3,1]
    s = 1
    print(S.containsNearbyDuplicate(num, s))
