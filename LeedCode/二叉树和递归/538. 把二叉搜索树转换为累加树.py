"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：
输入: 二叉搜索树:
              5
            /   \
           2     13
输出: 转换为累加树:
             18
            /   \
          20     13
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def __init__(self):
        self.last = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        self.convertBST(root.right)
        root.val = self.last + root.val
        self.last = root.val
        self.convertBST(root.left)
        return root