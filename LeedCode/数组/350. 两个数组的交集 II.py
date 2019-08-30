"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
"""


class Solution:
    def intersect(self, nums1, nums2):
        # dict1 = {}
        # for i in nums1:
        #     if i not in dict1:
        #         dict1[i] = 1
        #     else:
        #         dict1[i] += 1
        #
        # res = []
        # for j in nums2:
        #     if j in dict1 and dict1[j] > 0:
        #         res.append(j)
        #         dict1[j] -= 1
        #
        # return res

        
        # 如果数组是排序的情况下
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        i, j = 0, 0
        res = []
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res



