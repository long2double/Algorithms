"""
给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。

示例 :
输入:
   1
    \
     3
    /
   2
输出:
1

解释:
最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
注意: 树中至少有2个节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def __init__(self):
        self.last = None
        self.diff = 2 ** 32
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root is None:
            return

        self.getMinimumDifference(root.left)
        if self.last is None:
            self.last = root.val
        else:
            self.diff = min(self.diff, abs(self.last - root.val))
            self.last = root.val
        self.getMinimumDifference(root.right)
        return self.diff

