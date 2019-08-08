# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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