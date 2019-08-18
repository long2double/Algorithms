"""
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return self.isEqual(pRoot.left, pRoot.right)

    def isEqual(self, lRoot, rRoot):
        if lRoot is None and rRoot is None:
            return True
        if lRoot is not None and rRoot is None:
            return False
        if lRoot is None and rRoot is not None:
            return False
        if lRoot.val == rRoot.val:
            return self.isEqual(lRoot.left, rRoot.right) and self.isEqual(lRoot.right, rRoot.left)
        else:
            return False