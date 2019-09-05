"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
输入:
   1
 /   \
2     3
 \
  5
输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def binaryTreePaths(self, root: TreeNode):
        if root is None:
            return

        self.path.append(str(root.val))
        if root.left is None and root.right is None:
            self.res.append('->'.join(self.path))
        self.binaryTreePaths(root.left)
        self.binaryTreePaths(root.right)
        self.path.pop()
        return self.res
