"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return
        self.Convert(pRootOfTree.left)
        if self.pHead is None:
            self.pHead = pRootOfTree
        else:
            pRootOfTree.left = self.pEnd
            self.pEnd.right = pRootOfTree

        self.pEnd = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.pHead