"""
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     # 返回对应节点TreeNode
#     def __init__(self):
#         self.res = []
#
#     def KthNode(self, pRoot, k):
#         # write code here
#         if pRoot is None:
#             return
#
#         self.mid_order(pRoot)
#         if 0 < k <= len(self.res):
#             return self.res[k - 1]
#
#     def mid_order(self, pRoot):
#         if pRoot is None:
#             return
#         self.mid_order(pRoot.left)
#         self.res.append(pRoot)
#         self.mid_order(pRoot.right)


class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.index = 0

    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None:
            return

        node = self.KthNode(pRoot.left, k)
        if node is not None:
            return node

        self.index += 1
        if self.index == k:
            return pRoot

        node = self.KthNode(pRoot.right, k)
        if node is not None:
            return node