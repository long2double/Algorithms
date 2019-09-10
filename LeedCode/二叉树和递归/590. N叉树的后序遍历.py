"""
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :
返回其后序遍历: [5,6,3,2,4,1].
"""

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.res = []

    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return

        for child in root.children:
            self.postorder(child)
        self.res.append(root.val)
        return self.res
    