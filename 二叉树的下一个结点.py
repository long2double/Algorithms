"""
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的
指针。
"""


# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None

        # 当前结点有右结点，且该右结点没有左结点，则右结点即为下一个结点；若该右结点有左结点，则最后的左结点为下一个结点。
        if pNode.right is not None:
            p = pNode.right
            while p.left is not None:
                p = p.left
            return p

        # 当前结点没有右结点，寻找第一个父结点使的该父结点的父结点的左结点等于该父结点，则该父结点的父节点即为下一个结点
        while pNode.next is not None:
            if pNode.next.left == pNode:
                return pNode.next
            else:
                pNode = pNode.next
        return None