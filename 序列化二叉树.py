"""
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.index = -1

    def Serialize(self, root):
        # write code here
        if root is None:
            return '#,'
        # self.s += root.val
        # self.Serialize(root.left)
        # self.Serialize(root.right)
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.index += 1
        li = s.split(',')
        if self.index > len(li):
            return None

        root = None
        if li[self.index] != '#':
            root = TreeNode(int(li[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
