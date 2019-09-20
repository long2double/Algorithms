"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:
输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
"""


class TNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.count = 0


class Solution(object):
    def __init__(self):
        self.count_small = 0

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        node_vec = []
        for i in range(len(nums) - 1, -1, -1):
            node_vec.append(TNode(nums[i]))

        count = [0]
        for i in range(1, len(nums)):
            self.count_small = 0
            self.findTree(node_vec[0], node_vec[i])
            count.append(self.count_small)
        return count[::-1]

    def findTree(self, root, value):
        if value.val <= root.val:
            root.count += 1
            if root.left is not None:
                self.findTree(root.left, value)
            else:
                root.left = value
        else:
            self.count_small += root.count + 1
            if root.right is not None:
                self.findTree(root.right, value)
            else:
                root.right = value