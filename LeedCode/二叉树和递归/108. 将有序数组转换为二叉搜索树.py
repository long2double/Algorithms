"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        length = len(nums) - 1
        return self.array2BST(nums, 0, length)

    def array2BST(self, nums, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.array2BST(nums, start, mid - 1)
        root.right = self.array2BST(nums, mid + 1, end)
        return root

