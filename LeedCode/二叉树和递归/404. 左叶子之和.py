"""
计算给定二叉树的所有左叶子之和。

示例：
    3
   / \
  9  20
    /  \
   15   7
在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sums = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is not None and root.left.left is None and root.left.right is None:
            self.sums += root.left.val
            self.sumOfLeftLeaves(root.right)
        else:
            self.sumOfLeftLeaves(root.left)
            self.sumOfLeftLeaves(root.right)
        return self.sums
