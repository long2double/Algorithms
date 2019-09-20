"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = -1
        r = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            elif mid == start or nums[mid - 1] != target:
                l = mid
                break
            else:
                end -= 1

        # 当不存在时，直接返回[-1, -1]，无需判断右侧
        if start > end:
            return [-1, -1]

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            elif mid == end or nums[mid + 1] != target:
                r = mid
                break
            else:
                start += 1

        return [l, r]

