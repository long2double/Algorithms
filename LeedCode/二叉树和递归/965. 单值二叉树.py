"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def __init__(self):
        self.flag = None

    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if self.flag is None:
            self.flag = root.val
        if self.flag != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)