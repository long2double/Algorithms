"""
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺
序打印，其他行以此类推。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []

        stack1 = []
        stack2 = []
        sub = []
        flag = True

        stack1.append(pRoot)
        while stack1 or stack2:
            res = []
            if flag:
                length1 = len(stack1)
                for i in range(length1):
                    cur_node = stack1.pop()
                    res.append(cur_node.val)
                    if cur_node.left is not None:
                        stack2.append(cur_node.left)
                    if cur_node.right is not None:
                        stack2.append(cur_node.right)
            else:
                length2 = len(stack2)
                for i in range(length2):
                    cur_node = stack2.pop()
                    res.append(cur_node.val)
                    if cur_node.right is not None:
                        stack1.append(cur_node.right)
                    if cur_node.left is not None:
                        stack1.append(cur_node.left)
            sub.append(res)
            flag = not flag
        return sub


