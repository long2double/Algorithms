"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
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
        self.res = False

    def hasPathSum(self, root: TreeNode, sums: int) -> bool:
        if root is not None:
            self.path.append(root.val)
            if root.left is None and root.right is None and sum(self.path) == sums:
                self.res = True
            self.hasPathSum(root.left, sums)
            self.hasPathSum(root.right, sums)
            self.path.pop()
        return self.res
