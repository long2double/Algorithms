"""
题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经
过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.path = []
        self.res = []

    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []

        self.path.append(root.val)
        if root.left is None and root.right is None and sum(self.path) == expectNumber:
            self.res.append(self.path[:])
        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        self.path.pop()
        return self.res