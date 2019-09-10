"""
给定一个 N 叉树，返回其节点值的前序遍历。
例如，给定一个 3叉树 :

返回其前序遍历: [1,3,5,6,2,4]。
"""


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.res = []

    def preorder(self, root: 'Node'):
        if root is None:
            return

        self.res.append(root.val)
        for child in root.children:
            self.preorder(child)
        return self.res
