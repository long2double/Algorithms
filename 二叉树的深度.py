"""
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        # 广度优先搜索
        # if pRoot is None:
        #     return 0
        # queue = []
        # queue.append(pRoot)
        # deep = 0
        # while queue:
        #     length = len(queue)
        #     deep += 1
        #     for i in range(length):
        #         cur_node = queue.pop(0)
        #         if cur_node.left is not None:
        #             queue.append(cur_node.left)
        #         if cur_node.right is not None:
        #             queue.append(cur_node.right)
        # return deep

        # 递归
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1