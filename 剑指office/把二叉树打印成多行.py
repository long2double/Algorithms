"""
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []

        sub = []
        queue = []
        queue.append(pRoot)

        while queue:
            length = len(queue)
            res = []
            for i in range(length):
                cur_node = queue.pop(0)
                res.append(cur_node.val)
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
            sub.append(res)
        return sub
